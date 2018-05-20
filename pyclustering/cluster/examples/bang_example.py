"""!

@brief Examples of usage and demonstration of abilities of BANG algorithm in cluster analysis.

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2018
@copyright GNU Public License

@cond GNU_PUBLIC_LICENSE
    PyClustering is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PyClustering is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
@endcond

"""


from pyclustering.cluster import cluster_visualizer;
from pyclustering.cluster.bang import bang, bang_visualizer;

from pyclustering.utils import read_sample;

from pyclustering.samples.definitions import SIMPLE_SAMPLES, FCPS_SAMPLES;


def template_clustering(data_path, levels, **kwargs):
    data = read_sample(data_path)

    bang_instance = bang(data, levels)
    bang_instance.process()

    clusters = bang_instance.get_clusters()
    noise = bang_instance.get_noise()
    blocks = bang_instance.get_level_blocks()

    if len(data[0]) == 2:
        bang_visualizer.show_level_blocks(data, blocks)

    #visualizer = cluster_visualizer()
    #visualizer.append_clusters(clusters, data)
    #visualizer.append_cluster(noise, marker='x')
    #visualizer.show()


def cluster_simple_sample():
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE1, 8)
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE2, 7)
    template_clustering(SIMPLE_SAMPLES.SAMPLE_SIMPLE3, 7)


cluster_simple_sample()