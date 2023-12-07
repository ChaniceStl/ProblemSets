drug_names = [
    "alben",
    "alora",
    "astra",
    "bexil",
    "bovir",
    "cetra",
    "cevis",
    "daxon",
    "dovix",
    "drova",
]

# Create a mapping for digits to characters
mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


# def predict(digits: str):
#     except_output = []
#     for drug in range(drug_names):
#         is_match = is_drug_name_match(drug_names[drug], digits)
#         if is_match:
#             except_output.append(drug_names[drug])
#     return except_output


# def is_drug_name_match(drug: str, test_input: str):
#     for num in range(test_input):
#         letters = mapping[num]
#         if letters in drug[num]:
#             return True
#         else:
#             return False


######### edited version ##########
def predict_2(digits: str):
    except_output = []
    for drug in drug_names:
        is_match = is_drug_name_match_2(drug, digits)
        if is_match:
            except_output.append(drug)

    print(
        "expect", except_output
    )  # expect ['alben', 'alora', 'astra', 'bexil', 'bovir', 'cetra', 'cevis']
    return except_output


def is_drug_name_match_2(drug: str, test_input: str):
    for idx, num in enumerate(test_input):
        letters = mapping[num]
        # loop through 'mapping' key value, compare letters to current drug name char
        # list_letter = [l for l in letters if drug[idx] == l]
        for l in letters:
            if drug[idx] == l:
                return True
        else:
            return False


test_input = "25"
expected_output = ["alben", "alora"]
print(predict_2(test_input) == expected_output)

# return a list of drug names or empty list when no names match the mapping of the input
# create a list of drug names that are matches
# create a function that can determine if a word is a match to the test input
#  single drug name
#  test_input iterate through each element and using the mapping object to access value of the key.
# return true/false (good/bad)
# the predict function will the list generation. and return the new list

# echo "# ProblemSets" >> README.md
#   git init
#   git add README.md
#   git commit -m "first commit"
#   git branch -M main
#   git remote add origin git@github.com:ChaniceStl/ProblemSets.git
#   git push -u origin main
