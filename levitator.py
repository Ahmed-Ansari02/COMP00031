if __name__ == '__main__':
    from acoustools.Levitator import LevitatorController
    from acoustools.Utilities import create_points, add_lev_sig, propagate_abs
    from acoustools.Solvers import wgs

    lev = LevitatorController(ids=(73,53))
    p = create_points(1,1,x=0,y=0,z=0)
    amplitudes = []
    for i in range(5, 0, -1):
        amplitudes.append((1/i)*wgs(p))

    
    for x in amplitudes:
        print(propagate_abs(x,p))
        print(x.shape)
        x = add_lev_sig(x)

        lev.levitate(x)
        print('Levitating...')
        input()
    print('Stopping...')
    lev.disconnect()
    print('Stopped')


