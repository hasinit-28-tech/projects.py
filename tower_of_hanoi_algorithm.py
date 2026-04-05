def hanoi_solver(n):
    
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []
    
    moves = []
    
    
    def record():
        moves.append(f"{source} {auxiliary} {target}")
    
    def move_disks(num, from_rod, to_rod, aux_rod):
        if num == 1:
            to_rod.append(from_rod.pop())
            record()
            return
        
        move_disks(num - 1, from_rod, aux_rod, to_rod)
        to_rod.append(from_rod.pop())
        record()
        move_disks(num - 1, aux_rod, to_rod, from_rod)
    
    
    record()
    
    move_disks(n, source, target, auxiliary)
    
    return "\n".join(moves)