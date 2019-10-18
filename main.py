nama = 'Alex'
equation = 'motion for fall in love'

print (f'equation {equation} oleh {nama}')

def count_high (percepatan, waktu):
    high = (percepatan*waktu*waktu)/2
    print (f'percepatan {percepatan/10}m/s^2 ditempuh dalam waktu = {waktu/60}')
    print (f'sehingga high = {high}m')
    return (percepatan*waktu*waktu)/2

high = count_high (10, 5 * 60)

def count_circle (phy, diameter):
    circle = (phy*diameter*diameter)/(2*2)
    print (f'phy {phy} dikali dengan diameter = {diameter}')
    print (f'sehingga circle = {circle}m*m')
    return (phy*diameter*diameter)/(2*2)

circle = count_circle (3/4, 4)
