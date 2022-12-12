
 

def test_eight_components(fmn_unauthorized):
    fmn_unauthorized.get("https://fmn.apps.ocp.stg.fedoraproject.org/")
    title = fmn_unauthorized.title
    assert title == "FMN"

def test_login(fmn_authorized):
    fmn_authorized.get("https://fmn.apps.ocp.stg.fedoraproject.org/")
    title = fmn_authorized.title
    assert title == "FMN"
