class footballer():
    run="running"
    sprint="sprinting"
    price=5000
    def __init__(self,foot="right"):
        self.position="WF"
        self.foot=foot
class basketboller():
    turnstile="turnstile"
    trey="there-point"
    price=7500
    def __init__(self):
         self.pos="pivot"
class multisporcu(basketboller,footballer):
    def __init__(self,foot):
        basketboller.__init__(self)
        footballer.__init__(self,foot)

mahmut=multisporcu("right")
print(mahmut.turnstile)

print(mahmut.run)
print(mahmut.price)
print(mahmut.position)
print(mahmut.pos)
print(mahmut.foot)
