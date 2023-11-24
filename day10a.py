def format_name(fname, lname):
    if fname == "" or lname == "":
        return "Please enter first name and last name."
    formatter_f_name = fname.title()
    formatter_l_name = lname.title()
    return f"{formatter_f_name} {formatter_l_name}"


print(format_name("gAUTAM", "ROY"))
