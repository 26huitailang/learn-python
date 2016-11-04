#!/usr/bin/env python
# -*- coding: utf-8 -*-
u = []
with open('AfterUnclass.txt', 'wb') as af:
    with open('UnclassifiedLicense.txt', 'rb') as f:
        for line in f.readlines():
            if 'Depends/ AAF/ AAFSDK/' in line or 'nomos:' in line:
                del line
            else:
                u.append(line)
    af.writelines(u)