def format_name(fname , lname):

    if fname == "" or lname == "":
        return "YOu didn't provide valid inputs."
    formated_fname = fname.title()
    formated_lname = lname.title()

    return f"result: {formated_fname} {formated_lname}"

print(format_name(input("what is your first name?"),input("what is you last name?")))