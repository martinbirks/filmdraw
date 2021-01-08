import argparse
import random

def parseArgs():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--count", help="number of categories to pick per member", type=int, default=2)
    parser.add_argument("--members", help="filename containing member names", default="members.txt")
    parser.add_argument("--categories", help="filename containing category names", default="categories.txt")
    parser.add_argument("--previous", help="filename containing previous picks", default="previous.txt")
    parser.add_argument("--output", help="filename to output new \"previous\" categories to", default="output.txt")
    return parser.parse_args()

def readFile(filename):
    returnList = [];
    file = open(filename, "r")
    for line in file:
        returnList.append(line.strip())

    return returnList

def parsePreviousCategoriesLists(rawPrevious):
    returnList = []
    for memberPrevious in rawPrevious:
        returnList.append(memberPrevious.split(","))
    return returnList;

def memberVsPreviousErrorCheck(members, previousCategories):
    if len(previousCategories) != 0 and len(members) != len(previousCategories):
        print ("Error: number of members not same as number of previous categories")
        exit(1);

    if len(previousCategories) > 0:
        previousCategoriesCount = len(previousCategories[0])
        for i in range(len(previousCategories)):
            if previousCategoriesCount != len(previousCategories[i]):
                print ("Error: different number of previous categories for " + members[i])
                exit(1)

def getMemberOptions(allCategories, excludedCategories):
    memberOptions = allCategories.copy()
    for excluded in excludedCategories:
        if excluded in memberOptions:
            memberOptions.remove(excluded)

    return memberOptions

def pick(options, n):
    optionsCopy = options.copy()
    picked = []
    for i in (range(n)):
        if len(optionsCopy) == 0:
            print ("Error: pick failed - try again")
            exit(1)
        choice = random.choice(optionsCopy)
        picked.append(choice)
        optionsCopy.remove(choice)
    return picked

def outputNewPreviousFile(previousCategories, memberChoices, filename):
    file = open(filename, "w")
    for i in range(len(previousCategories)):
        file.write(",".join(previousCategories[i] + memberChoices[i]) + "\n")

def main():
    args = parseArgs()
    memberNames = readFile(args.members)
    categories = readFile(args.categories)
    rawPrevious = readFile(args.previous)

    previousCategories = parsePreviousCategoriesLists(rawPrevious)
    memberVsPreviousErrorCheck(memberNames, previousCategories)

    remainingCategories = categories.copy()
    memberChoices = []
    for i in range(len(memberNames)):
        memberOptions = getMemberOptions(remainingCategories, previousCategories[i])
        memberChoices.append(pick(memberOptions, args.count))
        for choice in memberChoices[i]:
            remainingCategories.remove(choice)

    for i in range(len(memberNames)):
        print (memberNames[i] + ": " + ", ".join(memberChoices[i]))

    outputNewPreviousFile(previousCategories, memberChoices, args.output)

main()