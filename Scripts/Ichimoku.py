class Ichimoku:
    def __init__(self, data, conversion_line_length, base_line_length, leading_span_b_length, lagging_span):
        self.data = data
        self.conversion_line_length = conversion_line_length
        self.base_line_length = base_line_length
        self.leading_span_b_length = leading_span_b_length
        self.lagging_span = lagging_span

    def create_data(self):
        tenken_sen = []
        size = self.data['High'].size
        for x in range(size-self.conversion_line_length):
            period_high_low = self.get_period_high_low(self.conversion_line_length, x)
            tenken_sen.append((period_high_low[0] + period_high_low[1]) / 2)

        return tenken_sen

    def get_period_high_low(self, conversion_line_length, x):

        if x == 0:
            max_period = self.data['High'][-conversion_line_length:].max()
            min_period = self.data['Low'][-conversion_line_length:].min()
        else:
            max_period = self.data['High'][-conversion_line_length - x:-x].max()
            min_period = self.data['Low'][-conversion_line_length - x:-x].min()

        print(max_period, min_period)
        return max_period, min_period
