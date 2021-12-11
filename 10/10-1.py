data = open("input10.txt").read().strip().split("\n")


test = [
'[({(<(())[]>[[{[]{<()<>>',
'[(()[<>])]({[<{<<[]>>(',
'{([(<{}[<>[]}>{[]{[(<()>',
'(((({<>}<{<{<>}{[]{[]{}',
'[[<[([]))<([[{}[[()]]]',
'[{[{({}]{}}([{[{{{}}([]',
'{<[[]]>}<{[{[{[]{()[[[]',
'[<(<(<(<{}))><([]([]()',
'<{([([[(<>()){}]>(<<{{',
'<{([{{}}[<[[[<>{}]]]>[]]',
]


def bracketPairs(lines):

    pairs = {"(":
    ")",
    "[":
     "]",
     "{":
      "}",
      "<":
       ">"}
    err_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    msg_points = {")": 1, "]": 2, "}": 3, ">": 4}
    err_scores = 0
    msg_scores = []

    for chunk in lines:
        score = 0
        leftPairs = []
        for c in chunk:
            if c in pairs.keys():
                leftPairs.append(c)
            else:
                if c == pairs[leftPairs[-1]]:
                    print('??',c, leftPairs[-1], pairs[leftPairs[-1]])
                    leftPairs.pop()
                else:
                    err_scores += err_points[c]
                    leftPairs = []
                    break
        if leftPairs:
            for m in [pairs[x] for x in leftPairs[::-1]]:
                score = (score * 5) + msg_points[m]
            msg_scores.append(score)

    print(f"Part 1: {err_scores}")
    print(f"Part 2: {sorted(msg_scores)[len(msg_scores)//2]}")



bracketPairs(test)