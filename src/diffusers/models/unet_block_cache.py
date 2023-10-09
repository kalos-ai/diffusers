class BlockCache:
    def __init__(
        self,
        downblock3_cache_refresh=4,
        downblock3_cache_start_ts=600,
        downblock3_cache_end_ts=100,
        midblock_cache_refresh=4,
        midblock_cache_start_ts=600,
        midblock_cache_end_ts=200,
    ):
        self.downblock3_cache = None
        self.downblock3_cache_count = 0
        self.midblock_cache = None
        self.midblock_cache_count = 0
        self.downblock3_cache_refresh = downblock3_cache_refresh
        self.midblock_cache_refresh = midblock_cache_refresh
        self.downblock3_cache_start_ts = downblock3_cache_start_ts
        self.downblock3_cache_end_ts = downblock3_cache_end_ts
        self.midblock_cache_start_ts = midblock_cache_start_ts
        self.midblock_cache_end_ts = midblock_cache_end_ts

    def read_downblock3_cache(self, ts):
        if ts > self.downblock3_cache_start_ts or ts < self.downblock3_cache_end_ts:
            return None
        if self.downblock3_cache_count < self.downblock3_cache_refresh:
            if self.downblock3_cache is not None:  #increase cache count
                self.downblock3_cache_count += 1
            return self.downblock3_cache
        return None

    def set_downblock3_cache(self, data, ts):
        if self.downblock3_cache_start_ts == 0:
            return
        if ts > self.downblock3_cache_start_ts or ts < self.downblock3_cache_end_ts:
            return
        if self.downblock3_cache is None:
            self.downblock3_cache = data

        if self.downblock3_cache_refresh >= self.downblock3_cache_count:
            self.downblock3_cache = data
        self.downblock3_cache_count = 0

    def read_midblock_cache(self, ts):
        if ts > self.midblock_cache_start_ts or ts < self.midblock_cache_end_ts:
            return None
        if self.midblock_cache_count < self.midblock_cache_refresh:
            if self.midblock_cache is not None:  #increase cache count
                self.midblock_cache_count += 1
            return self.midblock_cache
        return None

    def set_midblock_cache(self, data, ts):
        if self.midblock_cache_start_ts == 0:
            return
        if ts > self.midblock_cache_start_ts or ts < self.midblock_cache_end_ts:
            return
        if self.midblock_cache  is None:
            self.midblock_cache = data

        if self.midblock_cache_refresh >= self.midblock_cache_count:
            self.midblock_cache = data
        self.midblock_cache_count = 0
    def free_cache(self):
        if self.downblock3_cache is not None:
            del self.downblock3_cache 
            self.downblock3_cache = None
        if self.midblock_cache is not None:
            del self.midblock_cache
            self.midblock_cache = None
        self.downblock3_cache_count = 0
        self.midblock_cache_count = 0
