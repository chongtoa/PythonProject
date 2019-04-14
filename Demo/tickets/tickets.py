# coding: utf-8
'''Train tickets query via command-line
Usage:
   tickets [-gdtkz] <from><to><date>
Options:
   -h, --help    显示帮助菜单
   -g            高铁
   -d            动车
   -t            特快
   -k            快速
   -z            直达
Example:
   tickets 南京 北京 2019-4-4
   tickets -dg 南京 北京 2019-4-5
'''
import re, requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init, Fore
from stations import stations

init()

class TrainCollection(object):
	header = '车次 出发/到达站 出发/到达时间 历时 一等坐 二等坐 软卧 硬卧 硬座'.split()

	def __init__(self, available_trains, options):
		"""查询到的火车班次集合
        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
		self.available_trains = available_trains
		self.options = options

	def _get_duration(self, row):
		duration = row.get('lishi').replace(':', '小时') + '分'
		if duration.startswitch('00'):
			return duration[4:]
		if duration.startswitch('0'):
			return duration[1:]
		return duration

	@property
	def trains(self):
		for raw_train in self.available_trains:
			train_no = raw_train['station_train_code']
			initial = train_no[0].lower()
			if not self.options or initial in self.options:
				train = [
					train_no,        
					'\n'.join([Fore.GREEN + raw_train['from_station_name'] + Fore.RESET,
							Fore.RED + raw_train['to_station_name'] + Fore.RESET]),
					'\n'.join([Fore.GREEN + raw_train['start_time'] + Fore.RESET,
							Fore.RED + raw_train['arrive_time'] + Fore.RESET]),
					self._get_duration(raw_train),
					raw_train['zy_num'],
					raw_train['ze_num'],
					raw_train['rw_num'],
					raw_train['yw_num'],
					raw_train['yz_num'],
					raw_train['wz_num'],
				]
				yield train

	def pretty_print(self):
		pt = PrettyTable()
		pt._set_field_names(self.header)
		for train in self.trains:
			pt.add_row(train)
		print(pt)
	
def cli():
    '''command-line interface'''
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    url = ('https://kyfw.12306.cn/otn/lcxxcx/query?'
           'purpose_codes=ADULT&queryDate={}&'
           'from_station={}&to_station={}').format(
                date, from_station, to_station
           )
    options = ''.join([
        key for key, value in arguments.items() if value is True
        ])
    r = requesets.get(url, verify=False)
    available_trains = r.join()['data']['datas']
    TrainCollection(available_trains, options).pretty_print()


if __name__ == '__main__':
    cli()
