# rsa-swap

公開鍵eと秘密鍵dを交換します

- encryptでデコードできる
- paddingは無視する

```
$ openssl genrsa > private.pem
$ python src/rsa_swap/main.py private.pem > private_swapped.pem
$ openssl rsautl -encrypt -inkey private.pem -in <(echo 'Hello!') -out encrypted.bin
$ openssl rsautl -encrypt -raw -inkey private_swapped.pem -in encrypted.bin | xxd
00000000: 0002 1ae2 c333 4036 f842 a7d0 bb6f 6752  .....3@6.B...ogR
00000010: d78f b0db 57d2 f81c 2ef6 1752 8a97 1274  ....W......R...t
00000020: 611d d953 1d87 c9ef a7db 2062 a6e1 9046  a..S...... b...F
00000030: baf9 4ac7 5789 7d24 4e6b 0e66 19e9 1ff5  ..J.W.}$Nk.f....
00000040: c270 1ab5 e466 600f d665 9b49 478f 7d13  .p...f`..e.IG.}.
00000050: dad6 46d9 bfc0 7825 ec59 cd48 ca3d 3664  ..F...x%.Y.H.=6d
00000060: 7efa 4e6b 1ddc 8bcf f072 986c 1813 188c  ~.Nk.....r.l....
00000070: 3da3 1965 e75d 783a 6a22 f4de 36b9 91db  =..e.]x:j"..6...
00000080: bfc4 eafd a478 f3e6 27e1 9263 9933 726b  .....x..'..c.3rk
00000090: ad0d 9532 9f03 3114 4a7e 3f95 ba05 5c55  ...2..1.J~?...\U
000000a0: c9c9 197f 33de 0113 88b9 8fdd af69 5c6a  ....3........i\j
000000b0: d6c7 4155 e0f3 828d c1fe 7cc8 c0a3 4c44  ..AU......|...LD
000000c0: 7b3c c8ae db46 794b b2e9 c52f 4a7b daf1  {<...FyK.../J{..
000000d0: b5fa 3e1a 05b5 ebb0 7a47 d427 0c3b 8542  ..>.....zG.'.;.B
000000e0: 84e1 7d11 7443 b635 a983 e5df 5d36 c468  ..}.tC.5....]6.h
000000f0: a023 45e2 9c2f 2959 0048 656c 6c6f 210a  .#E../)Y.Hello!.
```
