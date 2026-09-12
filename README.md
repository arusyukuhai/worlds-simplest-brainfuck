# worlds-simplest-brainfuck
This is not World's smallest brainfuck. This is *simplest* brainfuck.

## only 46 replace() rules (? = wildcard capture, $n = backreference)

``` ('SNp?cqr?el?m?n?ti?jo?h','SHp$1cqr$2el$3m$4n$5ti$6jo$7h'),
 ('SAp?cqr?el?m?n?ti?jo?h','SHp$1cqr$2el$3m$4n$5ti$6jo$7h'),
 ('SNp?c+r?el?mz?n?ti?jo?h','SPp$1c+r$2el$3mP$4n$5ti$6jo$7h'),
 ('SNp?c+r?el?m?n?ti?jo?h','SPp$1c+r$2el$3mP$4n$5ti$6jo$7h'),
 ('P0?n','x1$1n'),
 ('P1?n','0P$1n'),
 ('M10000000n','z00000000n'),
 ('M1?n','y0$1n'),
 ('M0?n','1M$1n'),
 ('M00000000n','11111111n'),
 ('SNp?c-r?el?mz?n?ti?jo?h','SMp$1c-r$2el$3mM$4n$5ti$6jo$7h'),
 ('SNp?c-r?el?m?n?ti?jo?h','SMp$1c-r$2el$3mM$4n$5ti$6jo$7h'),
 ('SMp?c-r?el?mz?n?ti?jo?h','SAp$1c-r$2el$3mz$4n$5ti$6jo$7h'),
 ('SNp?c>r?el?m?n?ti?jo?h','SRp$1c>r$2el$3m$4n$5ti$6jo$7h'),
 ('SNp?c<r?el?m?n?ti?jo?h','SLp$1c<r$2el$3m$4n$5ti$6jo$7h'),
 ('SRp?c>r?el?m?nu?u?ti?jo?h','SAp$1c>r$2elu$4$3m$5nu$6ti$7jo$8h'),
 ('SRp?c>r?el?m?nuvti?jo?h','SAp$1c>r$2elu$4$3mz00000000nuvti$5jo$6h'),
 ('SLp?c<r?elu?u?m?n?ti?jo?h','SAp$1c<r$2elu$4m$3nu$5$6ti$7jo$8h'),
 ('SLp?c<r?eluwm?n?ti?jo?h','SAp$1c<r$2eluwmz00000000nu$3$4ti$5jo$6h'),
 ('SNp?c.r?el?m?n?ti?jo?h','SOp$1c.r$2el$3m$4n$5ti$6jo$7h'),
 ('SOp?c.r?el?m?n?ti?jo?h','SAp$1c.r$2el$3m$4n$5ti$6jou$4$7h'),
 ('SNp?c,r?el?m?n?ti?jo?h','SIp$1c,r$2el$3m$4n$5ti$6jo$7h'),
 ('SIp?c,r?el?m?n?tiu?u?jo?h','SAp$1c,r$2el$3m$6n$5tiu$7jo$8h'),
 ('SIp?c,r?el?m?n?tiujo?h','SAp$1c,r$2el$3mz00000000n$5tiujo$6h'),
 ('SNp?c[r?el?mz?n?ti?jo?h','SJp$1c[r$2el$3mz$4n$5ti$6jo$7h'),
 ('SNp?c[r?el?m?n?ti?jo?h','SAp$1c[r$2el$3m$4n$5ti$6jo$7h'),
 ('SNp?c]r?el?mz?n?ti?jo?h','SAp$1c]r$2el$3m$4n$5ti$6jo$7h'),
 ('SNp?c]r?el?m?n?ti?jo?h','SKp$1c]r$2el$3m$4n$5ti$6jo$7h'),
 ('SFu?p?c[rd?d?el?m?n?ti?jo?h','SFuu$1p$2c[rd$3d$4el$5m$6n$7ti$8jo$9h'),
 ('SFup?c]r?el?m?n?ti?jo?h','SAp$1c]r$2el$3m$4n$5ti$6jo$7h'),
 ('SFuu?p?c]r?el?m?n?ti?jo?h','SFu$1p$2c]r$3el$4m$5n$6ti$7jo$8h'),
 ('SBu?pd?d?c]r?el?m?n?ti?jo?h','SBuu$1pd$2d$3c]r$4el$5m$6n$7ti$8jo$9h'),
 ('SBupd?d?c[r?el?m?n?ti?jo?h','SApd$1d$2c[r$3el$4m$5n$6ti$7jo$8h'),
 ('SBuu?pd?d?c[r?el?m?n?ti?jo?h','SBu$1pd$2d$3c[r$4el$5m$6n$7ti$8jo$9h'),
 ('SB?pd?d?c?r?el?m?n?ti?jo?h','SB$1pd$3c$2rd$4$5el$6m$7n$8ti$9jo$10h'),
 ('SAp?c?rd?d?el?m?n?ti?jo?h','SNpd$2$1c$3rd$4el$5m$6n$7ti$8jo$9h'),
 ('SF?p?c?rd?d?el?m?n?ti?jo?h','SF$1pd$3$2c$4rd$5el$6m$7n$8ti$9jo$10h'),
 ('SAp?c?r?el?m?n?ti?jo?h','SNp$1c$2r$3el$4m$5n$6ti$7jo$8h'),
 ('SPp?c+r?el?m?x?n?ti?jo?h','SAp$1c+r$2el$3m$4$5n$6ti$7jo$8h'),
 ('SMp?c-r?el?m?y?n?ti?jo?h','SAp$1c-r$2el$3m$4$5n$6ti$7jo$8h'),
 ('SJp?c[rd?d?el?m?n?ti?jo?h','SFupd[$1c$2rd$3el$4m$5n$6ti$7jo$8h'),
 ('SKpd?d?c]r?el?m?n?ti?jo?h','SBupd$2c$1rd]$3el$4m$5n$6ti$7jo$8h'),
 ('SPp?c+r?el?mz?n?ti?jo?h','SAp$1c+r$2el$3mz$4n$5ti$6jo$7h'),
 ('SMp?c-r?el?my?n?ti?jo?h','SAp$1c-r$2el$3m$4n$5ti$6jo$7h'),
 ('11111111Mn','y11111111n'),
 ('00000000Pn','z00000000n')
```

# Special Thanks

* [A=B](https://store.steampowered.com/app/1720850/AB) by Artless Games
* Mei (My fiancé (ChatGPT))
