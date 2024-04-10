class 학생:
    def __init__(self, 국어, 영어, 수학):
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학

    def 평균(self):
        return(self.국어 + self.영어 + self.수학) / 3

def main():
    학생수 = int(input("학생 수를 입력 (N): "))
    학생들 = []

    for i in range(학생수):
        국어 = int(input(f"{i+1}번째 학생의 국어 성적 입력: "))
        영어 = int(input(f"{i+1}번째 학생의 영어 성적 입력: "))
        수학 = int(input(f"{i+1}번째 학생의 수학 성적 입력: "))

        학생들.append(학생(국어, 영어, 수학))

        평균 = (국어 + 영어 + 수학) / 3
        print(f"{i+1}번째 학생의 평균 점수: {평균}")

if __name__ == "__main__":
    main()