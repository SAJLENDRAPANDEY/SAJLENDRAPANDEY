import os
import json
import urllib.request
from datetime import datetime, timedelta, timezone
from html import escape


USERNAME = os.getenv("GITHUB_USERNAME", "SAJLENDRAPANDEY")
TOKEN = os.getenv("GITHUB_TOKEN")

OUTPUT = "assets/github-activity-overview.svg"


QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {

      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions

      repositoriesContributedTo: repositoriesContributedTo(
        first: 31
        contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]
      ) {
        totalCount
        nodes {
          nameWithOwner
        }
      }
    }
  }
}
"""


def github_graphql(query, variables):
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN is missing.")

    payload = json.dumps({
        "query": query,
        "variables": variables
    }).encode("utf-8")

    request = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "github-activity-overview"
        },
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    if "errors" in result:
        raise RuntimeError(json.dumps(result["errors"], indent=2))

    return result["data"]["user"]["contributionsCollection"]


def percentage(value, total):
    if total == 0:
        return 0

    return round((value / total) * 100)


def polar_to_cartesian(cx, cy, radius, angle):
    import math

    angle -= 90

    radians = math.radians(angle)

    return (
        cx + radius * math.cos(radians),
        cy + radius * math.sin(radians)
    )


def polygon_points(cx, cy, radius, values):
    points = []

    for i, value in enumerate(values):
        angle = i * 90
        x, y = polar_to_cartesian(cx, cy, radius * value, angle)
        points.append(f"{x:.2f},{y:.2f}")

    return " ".join(points)


def generate_svg(data):
    commits = data["totalCommitContributions"]
    issues = data["totalIssueContributions"]
    prs = data["totalPullRequestContributions"]
    reviews = data["totalPullRequestReviewContributions"]

    total = commits + issues + prs + reviews

    commit_pct = percentage(commits, total)
    issue_pct = percentage(issues, total)
    pr_pct = percentage(prs, total)
    review_pct = percentage(reviews, total)

    percentages = [
        commit_pct,
        pr_pct,
        issue_pct,
        review_pct
    ]

    repositories = data["repositoriesContributedTo"]

    repo_names = [
        node["nameWithOwner"]
        for node in repositories["nodes"]
    ]

    repo_count = repositories["totalCount"]

    first_repos = repo_names[:3]

    if len(first_repos) == 0:
        contribution_text = "No recent repository contributions"
    else:
        contribution_text = (
            "Contributed to "
            + ", ".join(first_repos)
        )

        remaining = max(repo_count - len(first_repos), 0)

        if remaining > 0:
            contribution_text += (
                f" and {remaining} other "
                f"repository{'ies' if remaining == 1 else 'ies'}"
            )

    width = 940
    height = 420

    cx = 720
    cy = 225
    radius = 110

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
    width="{width}"
    height="{height}"
    viewBox="0 0 {width} {height}">

    <rect
        x="8"
        y="8"
        width="{width - 16}"
        height="{height - 16}"
        rx="4"
        fill="#0d1117"
        stroke="#30363d"
        stroke-width="1"
    />

    <style>
        text {{
            font-family:
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                Helvetica,
                Arial,
                sans-serif;
        }}

        .title {{
            fill: #f0f6fc;
            font-size: 20px;
            font-weight: 500;
        }}

        .repo {{
            fill: #58a6ff;
            font-size: 16px;
            font-weight: 500;
        }}

        .normal {{
            fill: #c9d1d9;
            font-size: 16px;
        }}

        .percentage {{
            fill: #f0f6fc;
            font-size: 15px;
            font-weight: 500;
        }}

        .label {{
            fill: #8b949e;
            font-size: 15px;
        }}
    </style>

    <!-- Header -->
    <text x="28" y="45" class="title">
        Activity overview
    </text>

    <!-- Vertical divider -->
    <line
        x1="475"
        y1="75"
        x2="475"
        y2="390"
        stroke="#30363d"
        stroke-width="1"
    />

    <!-- Contribution text -->
    <text x="28" y="105" class="normal">
        {escape("Contributed to")}
    </text>
"""

    y = 135

    for repo in first_repos:
        svg += f"""
        <text x="58" y="{y}" class="repo">
            {escape(repo)}
        </text>
        """
        y += 30

    remaining = max(repo_count - len(first_repos), 0)

    if remaining > 0:
        svg += f"""
        <text x="58" y="{y}" class="normal">
            and {remaining} other repositories
        </text>
        """

    # Radar grid
    for scale in [0.25, 0.5, 0.75, 1.0]:
        pts = polygon_points(
            cx,
            cy,
            radius * scale,
            [1, 1, 1, 1]
        )

        svg += f"""
        <polygon
            points="{pts}"
            fill="none"
            stroke="#30363d"
            stroke-width="1"
        />
        """

    # Axis lines
    axis_points = [
        polar_to_cartesian(cx, cy, radius, 0),
        polar_to_cartesian(cx, cy, radius, 90),
        polar_to_cartesian(cx, cy, radius, 180),
        polar_to_cartesian(cx, cy, radius, 270)
    ]

    for x, y_axis in axis_points:
        svg += f"""
        <line
            x1="{cx}"
            y1="{cy}"
            x2="{x:.2f}"
            y2="{y_axis:.2f}"
            stroke="#30363d"
            stroke-width="1"
        />
        """

    # Actual activity polygon
    values = [p / 100 for p in percentages]

    activity_points = polygon_points(
        cx,
        cy,
        radius,
        values
    )

    svg += f"""
    <polygon
        points="{activity_points}"
        fill="#238636"
        fill-opacity="0.25"
        stroke="#3fb950"
        stroke-width="3"
        stroke-linejoin="round"
    />
    """

    # Center point
    svg += f"""
    <circle
        cx="{cx}"
        cy="{cy}"
        r="5"
        fill="#3fb950"
    />
    """

    # Labels
    svg += f"""
    <!-- Commit -->
    <text x="{cx}" y="92" text-anchor="middle" class="percentage">
        {commit_pct}%
    </text>
    <text x="{cx}" y="112" text-anchor="middle" class="label">
        Commits
    </text>

    <!-- Pull Requests -->
    <text x="720" y="405" text-anchor="middle" class="percentage">
        {pr_pct}%
    </text>
    <text x="720" y="423" text-anchor="middle" class="label">
        Pull requests
    </text>

    <!-- Issues -->
    <text x="870" y="220" text-anchor="middle" class="percentage">
        {issue_pct}%
    </text>
    <text x="870" y="240" text-anchor="middle" class="label">
        Issues
    </text>

    <!-- Reviews -->
    <text x="570" y="220" text-anchor="middle" class="percentage">
        {review_pct}%
    </text>
    <text x="570" y="240" text-anchor="middle" class="label">
        Code review
    </text>

    </svg>
    """

    return svg


def main():
    now = datetime.now(timezone.utc)
    one_year_ago = now - timedelta(days=365)

    data = github_graphql(
        QUERY,
        {
            "login": USERNAME,
            "from": one_year_ago.isoformat(),
            "to": now.isoformat()
        }
    )

    svg = generate_svg(data)

    os.makedirs("assets", exist_ok=True)

    with open(OUTPUT, "w", encoding="utf-8") as file:
        file.write(svg)

    print("GitHub Activity Overview updated successfully.")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
