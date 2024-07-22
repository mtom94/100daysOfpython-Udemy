def format_name(fname, lname):
    formated_fname = fname.title()
    formated_lname = lname.title()
    return f"{formated_fname} {formated_lname}"

result = format_name("MeERa" , "ThomAS")
print(result)
