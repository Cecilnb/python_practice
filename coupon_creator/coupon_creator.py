import random
import string

def generate_activation_code(length):
    characters = string.ascii_uppercase + string.digits
    return '-'.join(''.join(random.choice(characters) for _ in range(4)) for _ in range(length//4))

num_codes = 200
code_length = 16  # 激活码的长度，你可以根据需要进行调整

activation_codes = [generate_activation_code(code_length) for _ in range(num_codes)]

output_file = "activation_codes.txt"
with open(output_file, "w") as file:
    for code in activation_codes:
        file.write(code + "\n")

print(f"{num_codes}个激活码已生成并保存到{output_file}文件中。")
