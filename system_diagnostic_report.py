import psutil


def main():
    cpu_usage, ram_usage, disk_usage = get_system_stats()
    #cpu_usage, ram_usage, disk_usage = 91, 92, 93

    cpu_performance, ram_performance, disk_performance = analyze_performance(
        cpu_usage, ram_usage, disk_usage
    )

    assessment = overall_assessment(cpu_performance, ram_performance, disk_performance)

    #  use for debugging:   "✓ NORMAL"    "⚠ WARNING"    "✗ CRITICAL"
    cpu_recommendation, ram_recommendation, disk_recommendation = (
        generate_recommendations(cpu_performance, ram_performance, disk_performance)
    )

    display_report(
        cpu_usage,
        ram_usage,
        disk_usage,
        cpu_performance,
        ram_performance,
        disk_performance,
        cpu_recommendation,
        ram_recommendation,
        disk_recommendation,
        assessment,
    )


def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    return cpu_usage, ram_usage, disk_usage


def analyze_performance(cpu_usage, ram_usage, disk_usage):
    cpu_performance = analyzer(cpu_usage)
    ram_performance = analyzer(ram_usage)
    disk_performance = analyzer(disk_usage)

    return cpu_performance, ram_performance, disk_performance


def analyzer(usage):
    if usage < 70:
        return "✓ NORMAL"
    elif usage < 90:
        return "⚠ WARNING"
    else:
        return "✗ CRITICAL"


def overall_assessment(cpu_performance, ram_performance, disk_performance):
    problems = []

    # CPU problems
    if cpu_performance == "⚠ WARNING":
        problems.append("high CPU usage")
    elif cpu_performance == "✗ CRITICAL":
        problems.append("critically high CPU usage")

    # RAM problems
    if ram_performance == "⚠ WARNING":
        problems.append("high memory usage")
    elif ram_performance == "✗ CRITICAL":
        problems.append("critically high memory usage")

    # DISK problems
    if disk_performance == "⚠ WARNING":
        problems.append("low available disk space")
    elif disk_performance == "✗ CRITICAL":
        problems.append("critically low disk space")

    # No problems
    if not problems:
        return "No major resource bottlenecks detected. Your system resources are currently within normal ranges."

    # One problem
    if len(problems) == 1:
        return f"Your system may be experiencing performance issues primarily due to {problems[0]}."
    # Multiple problems
    elif len(problems) == 2:
        return f"Your system may be experiencing performance issues due to {problems[0]} and {problems[1]}."
    else:
        return f"Your system may be experiencing performance issues due to {problems[0]}, {problems[1]} and {problems[2]}."


def generate_recommendations(cpu_performance, ram_performance, disk_performance):
    cpu_recommendation = generate_cpu_recommendations(cpu_performance)
    ram_recommendation = generate_ram_recommendations(ram_performance)
    disk_recommendation = generate_disk_recommendations(disk_performance)

    return cpu_recommendation, ram_recommendation, disk_recommendation


def generate_cpu_recommendations(cpu_performance):
    if cpu_performance == "⚠ WARNING":
        return (
            "CPU usage is high. Close unnecessary applications or background processes."
        )
    elif cpu_performance == "✗ CRITICAL":
        return "CPU usage is critically high. Close resource-intensive applications and check for processes consuming excessive CPU."


def generate_ram_recommendations(ram_performance):
    if ram_performance == "⚠ WARNING":
        return "Memory usage is high. Close unnecessary applications and browser tabs to free up RAM."
    elif ram_performance == "✗ CRITICAL":
        return "Memory usage is critically high. Close memory-intensive applications and unnecessary browser tabs to free up RAM."


def generate_disk_recommendations(disk_performance):
    if disk_performance == "⚠ WARNING":
        return "Disk space is getting low. Consider removing unnecessary files or uninstalling unused applications."
    elif disk_performance == "✗ CRITICAL":
        return "Disk space is critically low. Free up storage by removing unnecessary files and applications."


def display_report(
    cpu_usage,
    ram_usage,
    disk_usage,
    cpu_performance,
    ram_performance,
    disk_performance,
    cpu_recommendation,
    ram_recommendation,
    disk_recommendation,
    assessment,
    ):
    print("""
╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                          SYSTEM DIAGNOSTIC REPORT                                                   ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
""")

    print("""
                                              RESOURCE STATUS
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

    print(
        f"CPU       {cpu_usage}%     {cpu_performance}\n"
        f"RAM       {ram_usage}%     {ram_performance}\n"
        f"Disk      {disk_usage}%     {disk_performance}"
    )

    print("""
                                           LIKELY PERFORMANCE ISSUES
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

    if cpu_performance == "⚠ WARNING":
        print("• CPU usage is high.")
    elif cpu_performance == "✗ CRITICAL":
        print("• CPU usage is critically high.")

    if ram_performance == "⚠ WARNING":
        print("• Memory usage is high.")
    elif ram_performance == "✗ CRITICAL":
        print("• Memory usage is critically high.")

    if disk_performance == "⚠ WARNING":
        print("• Disk space is getting low.")
    elif disk_performance == "✗ CRITICAL":
        print("• Disk space is critically low.")

    if (
        cpu_performance == "✓ NORMAL"
        and ram_performance == "✓ NORMAL"
        and disk_performance == "✓ NORMAL"
    ):
        print("• No major performance issues detected.")

    print("""
                                                RECOMMENDATIONS
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

    if cpu_recommendation:
        print(f"→ {cpu_recommendation}")

    if ram_recommendation:
        print(f"→ {ram_recommendation}")

    if disk_recommendation:
        print(f"→ {disk_recommendation}")

    if not any([
        cpu_recommendation,
        ram_recommendation,
        disk_recommendation
    ]):
        print("→ No recommendations. Your system resources are within normal ranges.")

    print("""
                                               OVERALL ASSESSMENT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

    if "No major" in assessment:
        print(f"✓ {assessment}")
    else:
        print(f"⚠ {assessment}")

    print("""
=======================================================================================================================
                                                END OF REPORT
=======================================================================================================================
""")

if __name__ == "__main__":
    main()
