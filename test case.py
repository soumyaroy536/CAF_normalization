from normalize import normalize_company_name

def test_normalize_company_name():
    assert normalize_company_name("CAF softsol") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("CAF solution") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("CAF           softSolution India Pvt Limited") == "CAF SoftSol India Pvt Ltd."
    assert normalize_company_name("") == "Company Name Not Available"
    assert normalize_company_name(None) == "Company Name Not Available"

    print("All test cases passed!")

test_normalize_company_name()
