import pytest
from system_diagnostic_report import analyze_performance, overall_assessment, generate_recommendations


# ============================================================
# TESTS FOR analyze_performance()
# ============================================================

def test_analyze_performance_all_normal():
    """Test when all resources are below 70%."""
    cpu_performance, ram_performance, disk_performance = analyze_performance(50, 60, 55)
    assert cpu_performance == "✓ NORMAL"
    assert ram_performance == "✓ NORMAL"
    assert disk_performance == "✓ NORMAL"


def test_analyze_performance_all_warning():
    """Test when all resources are between 70% and 89%."""
    cpu_performance, ram_performance, disk_performance = analyze_performance(75, 80, 85)
    assert cpu_performance == "⚠ WARNING"
    assert ram_performance == "⚠ WARNING"
    assert disk_performance == "⚠ WARNING"


def test_analyze_performance_all_critical():
    """Test when all resources are 90% and above."""
    cpu_performance, ram_performance, disk_performance = analyze_performance(95, 98, 97)
    assert cpu_performance == "✗ CRITICAL"
    assert ram_performance == "✗ CRITICAL"
    assert disk_performance == "✗ CRITICAL"


def test_analyze_performance_mixed():
    """Test with mixed performance levels."""
    cpu_performance, ram_performance, disk_performance = analyze_performance(42, 91, 78)
    assert cpu_performance == "✓ NORMAL"
    assert ram_performance == "✗ CRITICAL"
    assert disk_performance == "⚠ WARNING"


def test_analyze_performance_boundary_values():
    """Test boundary values: 69%, 70%, 89%, 90%."""
    cpu_performance, ram_performance, disk_performance = analyze_performance(69, 70, 89)
    assert cpu_performance == "✓ NORMAL"
    assert ram_performance == "⚠ WARNING"
    assert disk_performance == "⚠ WARNING"

    cpu_performance, ram_performance, disk_performance = analyze_performance(90, 95, 100)
    assert cpu_performance == "✗ CRITICAL"
    assert ram_performance == "✗ CRITICAL"
    assert disk_performance == "✗ CRITICAL"


# ============================================================
# TESTS FOR overall_assessment()
# ============================================================

def test_assessment_no_problems():
    """Test when all resources are NORMAL."""
    result = overall_assessment("✓ NORMAL", "✓ NORMAL", "✓ NORMAL")
    expected = "No major resource bottlenecks detected. Your system resources are currently within normal ranges."
    assert result == expected


def test_assessment_single_problem_cpu_warning():
    """Test when only CPU has WARNING."""
    result = overall_assessment("⚠ WARNING", "✓ NORMAL", "✓ NORMAL")
    expected = "Your system may be experiencing performance issues primarily due to high CPU usage."
    assert result == expected


def test_assessment_single_problem_cpu_critical():
    """Test when only CPU has CRITICAL."""
    result = overall_assessment("✗ CRITICAL", "✓ NORMAL", "✓ NORMAL")
    expected = "Your system may be experiencing performance issues primarily due to critically high CPU usage."
    assert result == expected


def test_assessment_single_problem_ram_warning():
    """Test when only RAM has WARNING."""
    result = overall_assessment("✓ NORMAL", "⚠ WARNING", "✓ NORMAL")
    expected = "Your system may be experiencing performance issues primarily due to high memory usage."
    assert result == expected


def test_assessment_single_problem_ram_critical():
    """Test when only RAM has CRITICAL."""
    result = overall_assessment("✓ NORMAL", "✗ CRITICAL", "✓ NORMAL")
    expected = "Your system may be experiencing performance issues primarily due to critically high memory usage."
    assert result == expected


def test_assessment_single_problem_disk_warning():
    """Test when only Disk has WARNING."""
    result = overall_assessment("✓ NORMAL", "✓ NORMAL", "⚠ WARNING")
    expected = "Your system may be experiencing performance issues primarily due to low available disk space."
    assert result == expected


def test_assessment_single_problem_disk_critical():
    """Test when only Disk has CRITICAL."""
    result = overall_assessment("✓ NORMAL", "✓ NORMAL", "✗ CRITICAL")
    expected = "Your system may be experiencing performance issues primarily due to critically low disk space."
    assert result == expected


def test_assessment_two_problems():
    """Test when two resources have problems."""
    result = overall_assessment("⚠ WARNING", "✗ CRITICAL", "✓ NORMAL")
    expected = "Your system may be experiencing performance issues due to high CPU usage and critically high memory usage."
    assert result == expected

    result = overall_assessment("⚠ WARNING", "✓ NORMAL", "⚠ WARNING")
    expected = "Your system may be experiencing performance issues due to high CPU usage and low available disk space."
    assert result == expected

    result = overall_assessment("✓ NORMAL", "⚠ WARNING", "⚠ WARNING")
    expected = "Your system may be experiencing performance issues due to high memory usage and low available disk space."
    assert result == expected


def test_assessment_three_problems():
    """Test when all three resources have problems."""
    result = overall_assessment("⚠ WARNING", "✗ CRITICAL", "⚠ WARNING")
    expected = "Your system may be experiencing performance issues due to high CPU usage, critically high memory usage and low available disk space."
    assert result == expected

    result = overall_assessment("✗ CRITICAL", "⚠ WARNING", "✗ CRITICAL")
    expected = "Your system may be experiencing performance issues due to critically high CPU usage, high memory usage and critically low disk space."
    assert result == expected

    result = overall_assessment("✗ CRITICAL", "✗ CRITICAL", "✗ CRITICAL")
    expected = "Your system may be experiencing performance issues due to critically high CPU usage, critically high memory usage and critically low disk space."
    assert result == expected


# ============================================================
# TESTS FOR generate_recommendations()
# ============================================================

def test_generate_recommendations_all_normal():
    """Test when all resources are NORMAL."""
    cpu_recommendation, ram_recommendation, disk_recommendation = generate_recommendations(
        "✓ NORMAL", "✓ NORMAL", "✓ NORMAL"
    )
    assert cpu_recommendation is None
    assert ram_recommendation is None
    assert disk_recommendation is None


def test_generate_recommendations_all_warning():
    """Test when all resources have WARNING status."""
    cpu_recommendation, ram_recommendation, disk_recommendation = generate_recommendations(
        "⚠ WARNING", "⚠ WARNING", "⚠ WARNING"
    )

    assert cpu_recommendation == "CPU usage is high. Close unnecessary applications or background processes."
    assert ram_recommendation == "Memory usage is high. Close unnecessary applications and browser tabs to free up RAM."
    assert disk_recommendation == "Disk space is getting low. Consider removing unnecessary files or uninstalling unused applications."


def test_generate_recommendations_all_critical():
    """Test when all resources have CRITICAL status."""
    cpu_recommendation, ram_recommendation, disk_recommendation = generate_recommendations(
        "✗ CRITICAL", "✗ CRITICAL", "✗ CRITICAL"
    )

    assert cpu_recommendation == "CPU usage is critically high. Close resource-intensive applications and check for processes consuming excessive CPU."
    assert ram_recommendation == "Memory usage is critically high. Close memory-intensive applications and unnecessary browser tabs to free up RAM."
    assert disk_recommendation == "Disk space is critically low. Free up storage by removing unnecessary files and applications."


def test_generate_recommendations_mixed():
    """Test with mixed performance statuses."""
    # Only RAM critical, disk warning
    cpu_recommendation, ram_recommendation, disk_recommendation = generate_recommendations(
        "✓ NORMAL", "✗ CRITICAL", "⚠ WARNING"
    )

    assert cpu_recommendation is None
    assert ram_recommendation == "Memory usage is critically high. Close memory-intensive applications and unnecessary browser tabs to free up RAM."
    assert disk_recommendation == "Disk space is getting low. Consider removing unnecessary files or uninstalling unused applications."

    # CPU warning, disk critical
    cpu_recommendation, ram_recommendation, disk_recommendation = generate_recommendations(
        "⚠ WARNING", "✓ NORMAL", "✗ CRITICAL"
    )

    assert cpu_recommendation == "CPU usage is high. Close unnecessary applications or background processes."
    assert ram_recommendation is None
    assert disk_recommendation == "Disk space is critically low. Free up storage by removing unnecessary files and applications."

    # CPU critical, RAM warning
    cpu_recommendation, ram_recommendation, disk_recommendation = generate_recommendations(
        "✗ CRITICAL", "⚠ WARNING", "✓ NORMAL"
    )

    assert cpu_recommendation == "CPU usage is critically high. Close resource-intensive applications and check for processes consuming excessive CPU."
    assert ram_recommendation == "Memory usage is high. Close unnecessary applications and browser tabs to free up RAM."
    assert disk_recommendation is None
