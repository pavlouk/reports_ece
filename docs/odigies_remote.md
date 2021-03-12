```plouk@paul MINGW64 ~
$ cd ανιχνευτής/
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$ ssh-keygen -t rsa -b 4096 -C "My CI Deploy"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/plouk/.ssh/id_rsa): deploykey
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in deploykey
Your public key has been saved in deploykey.pub
The key fingerprint is:
SHA256:VaQ0iy4WiEqizDBUCZARNZZajPZNjaUF7uyn7eyVftw My CI Deploy
The key's randomart image is:
+---[RSA 4096]----+
|=X*o..=o  o.o    |
|+o++.+o. o =     |
|=+o +o. . +      |
|Oo .o. o .       |
|oo   oo S        |
|    .. .  .      |
|     . . o. .    |
|      = o  o E   |
|     .o= ..      |
+----[SHA256]-----+
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$ git config --global url."git@gitlab.com:".insteadOf "https://gitlab.com/"
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$ mkdir -p ~/.ssh && chmod 700 ~/.ssh
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$ ssh-keyscan -H gitlab.com >> ~/.ssh/known_hosts
# gitlab.com:22 SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2
# gitlab.com:22 SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2
# gitlab.com:22 SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2
# gitlab.com:22 SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2
# gitlab.com:22 SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$ chmod 400 deploykey
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$ eval $(ssh-agent -s)
Agent pid 118
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$ ssh-add deploykey
Identity added: deploykey (My CI Deploy)
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$ git clone https://gitlab.com/ploukareas/adipose-detector
Cloning into 'adipose-detector'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.
(base)
plouk@paul MINGW64 ~/ανιχνευτής (master)
$```
