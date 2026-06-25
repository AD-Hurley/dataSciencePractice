import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--physics', type=float, help='physics grade')
    parser.add_argument('--chemistry', type=float, help='chemistry grade')
    parser.add_argument('--math', type=float, help='math grade')

    args = parser.parse_args()

    physGrade = args.physics
    chemistryGrade = args.chemistry
    mathGrade = args.math

    avg = (physGrade + chemistryGrade + mathGrade) / 3

    print("Average Grade: "+str(round(avg, 2)))
