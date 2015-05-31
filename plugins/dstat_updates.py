class dstat_plugin(dstat):
    """
    Amount of used and free space per mountpoint.
    """

    def __init__(self):

        #/usr/lib/update-notifier/apt-check --human-readable

        #13 packages can be updated.
        #0 updates are security updates.

        self.name = "updates"
        self.nick = ('upd', 'sec')
        self.vars = ('updv', 'secv')
        self.type = 's'
        self.scale = 0
        self.seconds_to_update = 24 * 60 * 60 #update once a day
        self.cnt = self.seconds_to_update

    def extract(self):
        if self.cnt < self.seconds_to_update:
            self.cnt += 1
            return
        for lyne in cmd_splitlines("/usr/lib/update-notifier/apt-check --human-readable", os.linesep):
            lyne = "".join(lyne)
            try:
                self.val['updv'] = re.search("(\d*) packages can be updated", lyne).group(1)
            except AttributeError:
                pass #value not found
            try:
                self.val['secv'] = re.search("(\d*) updates are security updates.", lyne).group(1)
            except AttributeError:
                pass #value not found
        self.cnt = 0


# vim:ts=4:sw=4:et
