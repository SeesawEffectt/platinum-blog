names = """1. Blazblue Centralfiction
2. Blazblue Chronophantasma
3. Kingdom Hearts Birth By Sleep
4. Lies of P
5. Kingdom Hearts 2
6. 2064 Read Only Memories
7. Kingdom Hearts: Re:Chain of Memories
8. Naruto Storm 2
9. Dragon Ball Xenoverse 2
10. Kingdom Hearts: Dream Drop Distance
11. Nioh
12. Street Fighter 6
13. Code Vein
14. Assassin's Creed 2
15. NEOTWEWY
16. Final Fantasy XV
17. Assassin's Creed Valhalla(PS4)
18. Assassin's Creed Valhalla(PS5)
19. Assassin's Creed 3
20. Assassin's Creed Syndicate
21. Assassin's Creed Odyssey
22. Kingdom Hearts
23. Assassin's Creed Origins
24. Assassin's Creed Rogue
25. Assassin's Creed Black Flag
26. Beyond Two Souls
27. Borderlands 2
28. Borderlands 3
29. Elden Ring(PS4)
30. Elden Ring(PS5)
31. Shadow of the Colossus
32. Kingdom Hearts 3
33. Brawlhalla
34. Street Fighter 6
35. Assassin's Creed Brotherhood
36. The Witness
37. Human Fall Flat
38. Persona 5
39. Rune Factory: Tides of Destiny
40. Assassin's Creed Revelations
41. Assassin's Creed Mirage
42. Persona 5 Royal
43. Goat Simulator
44. Danganronpa 1-2 Reload
45. Guilty Gear Strive
46. Final Fantasy VII
47. Sly Cooper 3
48. Sonic Frontiers
49. Tekken 7
50. Ark Survival Evolved
51. Nitroplus Blasterz
52. Multiversus
53. Minecraft
54. Crossovers
55. Naruto Storm 3
56. Naruto Storm 4
57. Sly Cooper 4
58. South Park: The Fractured But Whole
59. Saints Row IV
60. Gat out of Hell
61. Tekken Tag Tournament 2
62. Bloodborne
63. Dust: An Elysian Tale
64. Adventure Time: Pirates of the Enchiridion
65. Zero Escape the Nonary Games
66. Zero Time Dilemma
67. Virtue's Last Reward
68. 428: Shibuya Scramble
69. Detroit: Become Human
70. Naruto Storm
71. Soul Calibur 6
72. Cat Quest 2
73. JoJo's Bizarre Adventure: All Star Battle
74. Cat Quest
75. Days Gone
76. Ratchet and Clank
77. Dark Souls 3
78. Demon's Souls
79. Dark Souls
80. Dark Souls 2
81. Sekiro
82. Jak 2
83. Jak 3
84. Jak X: Combat Racing
85. 13 Sentinels: Aegis Rim
86. Blazblue Calamity Trigger
87. Cars Race-O-Rama
88. DOOM(2016)
89. Skyrim
90. Spiderman: Miles Morales
91. Spiderman 2
92. The Sims 4
93. One Piece: Pirate Warriors 4
94. Magus
95. Stories: Path of Destinies
96. Word Sudoku
97. Rime
98. Heavy Rain
99. Dragon Quest 11 S
100. Dragon Quest 11: Echoes of an Illusory Age
101. Minecraft Dungeons
102. Sly Cooper 2
103. Battle for Bikini Bottom: Rehydrated
104. Bugsnax
105. The Wolf Among Us
106. Claire
107. DDLC+
108. Batman: The Enemy Within
109. Undertale
110. Peasant Knight
111. Conan Exiles
112. Spiderman
113. South Park Stick of Truth
114. Melty Blood: Type Lumina
115. Jack and Daxter: The Lost Frontier
116. Ice Age: Scrat's Nutty Adventure
117. Astro's Playroom
118. Little Nightmares II
119. Paradise Killer
120. Ai: The Somnium Files: NirvanA Initiative
121. Ai: The Somnium Files
122. Jak and Daxter: The Precursor Legacy(Vita)
123. Jak and Daxter: The Precursor Legacy(PS4)
124. Daxter
125. Sly Cooper
126. Blazblue Crosstag Battle
127. Shiin
128. My Friend Peppa Pig
129. Psychopass Mandatory Happiness
130. JoJo's Eyes of Heaven
131. Miko Gakkou Monogatari: Kaede Episode
132. My Name is Mayo(PS4)
133. My Name is Mayo(Vita)
134. Punch Line
135. Batman Telltale
136. Jack and Jill DX
137. Burly Men at Sea
"""
names = names.splitlines()
y = []
for x in names:
    x = x.split(' ')
    x = x[1:]
    x = " ".join(x)
    y.append(x)
for x in y:
    print(f'<div class="icon"><img src=blazbluecf.jpg width=250 height=250 title="{x}"></img></div>')