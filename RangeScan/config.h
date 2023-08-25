// We initially had 1M tuples == 4MB input data, targetting L3 Cache.
// However, on cascadelake, L3 bandwidth was bottlenecking, so we went down to ~125kB, targetting L2.
static constexpr size_t NUM_BASE_ROWS = 16;
static constexpr size_t SCALE_FACTOR = 1024ull * 1;
static constexpr size_t NUM_ROWS = NUM_BASE_ROWS * SCALE_FACTOR;
static constexpr size_t NUM_UNIQUE_VALUES = 16;