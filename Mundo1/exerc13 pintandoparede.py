larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
area = larg * alt
print('sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(larg, alt, area))
tinta = area/2
print('para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))