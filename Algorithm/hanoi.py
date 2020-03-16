def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 0 :
        return None
    num_poles = [1, 2, 3]
    num_poles.remove(start_peg)
    num_poles.remove(end_peg)
    possible_pole = num_poles[0]

    hanoi(num_disks - 1, start_peg, possible_pole) # n - 1
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, possible_pole, end_peg)

# 테스트 코드 (포함하여 제출해주세요)
hanoi(4, 1, 3)