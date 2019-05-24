#include <cstring>
#define Cpy(a, b) memcpy(a, b, sizeof(a))
#define Set(a, v) memset(a, v, sizeof(a))
#define debug(x) cout << #x << ": " << x << endl
#define _rep(i, l, r) for (int i = (l); i <= (r); i++)
#define _for(i, l, r) for (int i = (l); i < (r); i++)
#define debug_(ch, i) printf(#ch "[%d]: %d\n", i, ch[i])
#define debug_m(mp, p) printf(#mp "[%d]: %d\n", p->first, p->second)