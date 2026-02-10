from datetime import datetime


def generate_markdown_report(findings, output_file="report.md"):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    severity_count = {}
    for f in findings:
        severity_count[f.severity.value] = severity_count.get(f.severity.value, 0) + 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Azure Cloud Security Assessment Report\n\n")
        f.write(f"**Generated:** {now}\n\n")

        f.write("## Executive Summary\n\n")
        if not findings:
            f.write("No security issues were identified during the assessment.\n\n")
        else:
            f.write(
                "This report contains security findings identified during an automated "
                "cloud security and identity assessment of the Azure subscription. "
                "The findings focus on identity misconfigurations, excessive privileges, "
                "and attack paths that could lead to full subscription compromise.\n\n"
            )

        f.write("### Findings Overview\n\n")
        for sev, count in severity_count.items():
            f.write(f"- **{sev}**: {count}\n")

        f.write("\n---\n\n")

        for finding in findings:
            f.write(f"## [{finding.severity.value}] {finding.title}\n\n")
            for detail in finding.details:
                f.write(f"- {detail}\n")
            f.write("\n---\n\n")

    print(f"[+] Report written to {output_file}")
