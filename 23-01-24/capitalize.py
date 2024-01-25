def capitalize_name(full_name):
    capitalized_name = full_name.title()
    print(capitalized_name)

if __name__ == '__main__':
    full_name = input().strip()
    capitalize_name(full_name)
