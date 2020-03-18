def test_vcftools(host):
    """
    Check vcftools version.
    """
    cmd = "vcftools --version"
    cmd_result = host.run(cmd)
    assert cmd_result.rc == 0, "'{}' returned status {}.".format(cmd, cmd_result.rc)
    assert "VCFtools (0.1.16000)" in cmd_result.stdout, f"'{cmd}' returned stdout '{cmd_result.stdout}', stderr '{cmd_result.stderr}'"
