"""Copyright (C) 2016  Jbdo99

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import random
from QuizzAPI import Quizz

qq = Quizz()

for i in range(random.randrange(1,10)):
    qq.add_quest(str(i),str(i))
    print ("Q"+i)



bcl = True
quest = random.choice(qq.all_question())
print ("Question : "+str(quest))
while bcl:
    rep = input("Reponse : ")
    if (qq.is_correct(quest,rep)==True):
        print("Vrai")
        bcl = False
    else:
        print("Faux")
