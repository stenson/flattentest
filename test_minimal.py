from fontTools.misc.bezierTools import calcQuadraticArcLength

# 107.70329614269008
print(calcQuadraticArcLength((0, 0), (50, 20), (100, 40)))

# 127.92252850725014
print(calcQuadraticArcLength((210, 333), (289, 333), (326.5, 290.5)))