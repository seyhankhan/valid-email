####### Seyhan Van Khan
####### Email Validator
####### Checks syntax of email & can be used modularly
####### 10 October 2018
""" FUNCTIONS:
        ValidEmail(email, valid_domains, valid_topleveldomains) -
        contains1of(email, character) - checks if email only has 1 of a certain character
        domain_name(email) - returns the email's domain name
"""
# Checks if email is valid with a valid domain & top level domain (tld)
def ValidEmail(email, valid_domains=None, valid_topleveldomains=None):
    valid_domains = ["gmail", "outlook", "hotmail", "yahoo"] if valid_domains is None else valid_domains
    valid_topleveldomains = [".com", ".co.uk", ".org", ".net"] if valid_topleveldomains is None else valid_topleveldomains

    for tld in valid_topleveldomains:
        if email[-len(tld):] == tld and contains1of(email, tld):
            valid_tld = True
            break
        else:
            valid_tld = False

    if (
    " " not in email
    and contains1of(email, "@") and email.find("@") > 1 and email.find("@") < 63
    and domain_name(email) in valid_domains
    and contains1of(email, ".")
    and valid_tld):
        return True
    else:
        return False

# Checks if email contains just 1 of a certain character
def contains1of(email, char):
    return email.count(char) == 1

# Returns email's domain name
def domain_name(email):
    return email[email.find("@") + 1:email.find(".")]
