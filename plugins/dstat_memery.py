class dstat_plugin(dstat):
    """
    Amount of used and free space per mountpoint.
    """

    def __init__(self):

        self.name = "memery"
        self.nick = ('slab', 'cache', 'rss')
        self.vars = ('slabv', 'cachev', 'rssv')
        self.type = 'b'
        #self.scale = 0

    def get_rss(self):
        for l in cmd_readlines("for i in /proc/*/status ; do grep VmRSS $i; done | awk '{ s = s + $2 } END { print s }'"):
            return long(l)

    def get_from_file(self, fname, string):
        with open(fname, "r") as f:
            for l in f.xreadlines():
                try:
                    return long(re.search(string, l).group(1))
                except:
                    pass #not the line we want

    def extract(self):
        self.val['rssv'] = self.get_rss()
        self.val['cachev'] = self.get_from_file("/proc/meminfo", "Cached:\s*(\d*)")
        self.val['slabv'] = self.get_from_file("/proc/meminfo", "Slab:\s*(\d*)")

# vim:ts=4:sw=4:et
