#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Scenario Classification Ml
# Generated: Tue Nov 21 02:17:17 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import classifier
import fbmc
import numpy as np
import scenario_classification_f
import sip
import sys
import threading
import time
from gnuradio import qtgui


class scenario_classification_ml(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Scenario Classification Ml")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Scenario Classification Ml")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "scenario_classification_ml")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.subchan_map = subchan_map = np.concatenate(([0,]*6, [1,]*116, [0,]*6))
        self.samp_rate = samp_rate = int(1e7)
        self.packetlen_base = packetlen_base = 256 * 8
        self.cfg = cfg = fbmc.fbmc_config(channel_map=(subchan_map), num_payload_bits=packetlen_base, num_overlap_sym=4, samp_rate=int(samp_rate)/4)
        self.taps = taps = np.array([0.003524782368913293, 0.002520402194932103, -3.532667373554307e-17, -0.0025783423334360123, -0.0036887258756905794, -0.0026390093844383955, -3.7046301165340785e-18, 0.0027025998570024967, 0.003868663916364312, 0.0027693307492882013, -9.712380039780164e-18, -0.0028394402470439672, -0.004067056812345982, -0.0029131921473890543, 2.454170927498071e-17, 0.0029908770229667425, 0.004286897834390402, 0.0030728192068636417, -9.712380039780164e-18, -0.0031593774911016226, -0.004531863145530224, -0.0032509532757103443, -6.861573196148834e-18, 0.0033479968551546335, 0.004806521814316511, 0.003451012307778001, -9.712380039780164e-18, -0.0035605679731816053, -0.005116619635373354, -0.0036773078609257936, 2.849619674016194e-17, 0.003801962360739708, 0.005469490308314562, 0.003935364540666342, -9.712380039780164e-18, -0.004078468773514032, -0.0058746375143527985, -0.004232373554259539, -1.196125168755972e-17, 0.004398348741233349, 0.006344608962535858, 0.004577873274683952, -9.712380039780164e-18, -0.004772676154971123, -0.0068963137455284595, -0.004984795115888119, 3.532667373554307e-17, 0.005216646008193493, 0.00755310570821166, 0.005471116863191128, -9.712380039780164e-18, -0.0057516866363584995, -0.00834816973656416, -0.00606258912011981, 9.712380039780164e-18, 0.006409022491425276, 0.009330307133495808, 0.006797448266297579, -9.712380039780164e-18, -0.007235993165522814, -0.010574348270893097, -0.007735027000308037, 9.712380039780164e-18, 0.008307991549372673, 0.012201170437037945, 0.008972631767392159, -9.712380039780164e-18, -0.00975286029279232, -0.014419564977288246, -0.010681704618036747, 9.712380039780164e-18, 0.011806094087660313, 0.017623912543058395, 0.013195047155022621, -9.712380039780164e-18, -0.01495438627898693, -0.022659316658973694, -0.017255060374736786, 9.712380039780164e-18, 0.020392345264554024, 0.03172304481267929, 0.02492397651076317, -9.712380039780164e-18, -0.03204511106014252, -0.052871737629175186, -0.04486315697431564, 9.712380039780164e-18, 0.0747719332575798, 0.15861520171165466, 0.22431577742099762, 0.24915219843387604, 0.22431577742099762, 0.15861520171165466, 0.0747719332575798, 9.712380039780164e-18, -0.04486315697431564, -0.052871737629175186, -0.03204511106014252, -9.712380039780164e-18, 0.02492397651076317, 0.03172304481267929, 0.020392345264554024, 9.712380039780164e-18, -0.017255060374736786, -0.022659316658973694, -0.01495438627898693, -9.712380039780164e-18, 0.013195047155022621, 0.017623912543058395, 0.011806094087660313, 9.712380039780164e-18, -0.010681704618036747, -0.014419564977288246, -0.00975286029279232, -9.712380039780164e-18, 0.008972631767392159, 0.012201170437037945, 0.008307991549372673, 9.712380039780164e-18, -0.007735027000308037, -0.010574348270893097, -0.007235993165522814, -9.712380039780164e-18, 0.006797448266297579, 0.009330307133495808, 0.006409022491425276, 9.712380039780164e-18, -0.00606258912011981, -0.00834816973656416, -0.0057516866363584995, -9.712380039780164e-18, 0.005471116863191128, 0.00755310570821166, 0.005216646008193493, 3.532667373554307e-17, -0.004984795115888119, -0.0068963137455284595, -0.004772676154971123, -9.712380039780164e-18, 0.004577873274683952, 0.006344608962535858, 0.004398348741233349, -1.196125168755972e-17, -0.004232373554259539, -0.0058746375143527985, -0.004078468773514032, -9.712380039780164e-18, 0.003935364540666342, 0.005469490308314562, 0.003801962360739708, 2.849619674016194e-17, -0.0036773078609257936, -0.005116619635373354, -0.0035605679731816053, -9.712380039780164e-18, 0.003451012307778001, 0.004806521814316511, 0.0033479968551546335, -6.861573196148834e-18, -0.0032509532757103443, -0.004531863145530224, -0.0031593774911016226, -9.712380039780164e-18, 0.0030728192068636417, 0.004286897834390402, 0.0029908770229667425, 2.454170927498071e-17, -0.0029131921473890543, -0.004067056812345982, -0.0028394402470439672, -9.712380039780164e-18, 0.0027693307492882013, 0.003868663916364312, 0.0027025998570024967, -3.7046301165340785e-18, -0.0026390093844383955, -0.0036887258756905794, -0.0025783423334360123, -3.532667373554307e-17, 0.002520402194932103])*2
        self.phydyas_taps_time = phydyas_taps_time = np.array(cfg.phydyas_impulse_taps(cfg.num_total_subcarriers(), cfg.num_overlap_sym()))
        self.nguard_bins = nguard_bins = 8
        self.nchan = nchan = 4
        self.sync = sync = fbmc.sync_config(taps=(phydyas_taps_time[1:]/np.sqrt(phydyas_taps_time.dot(phydyas_taps_time))), N=cfg.num_total_subcarriers(), overlap=4, L=cfg.num_total_subcarriers()-1, pilot_A=1.0, pilot_timestep=4, pilot_carriers=(range(8, 118, 12) + [119]), subbands=nchan, bits=packetlen_base, pos=4, u=1, q=4, A=1.0 , fft_len=2**13, guard=nguard_bins)
        self.su_frame_len_low_rate = su_frame_len_low_rate = sync.get_frame_samps(True)
        self.SNR_ch_4 = SNR_ch_4 = 0
        self.SNR_ch_3 = SNR_ch_3 = 0
        self.SNR_ch_2 = SNR_ch_2 = 0
        self.SNR_ch_1 = SNR_ch_1 = 0
        self.variable_qtgui_label_3_2 = variable_qtgui_label_3_2 = SNR_ch_4
        self.variable_qtgui_label_3_1 = variable_qtgui_label_3_1 = SNR_ch_3
        self.variable_qtgui_label_3_0 = variable_qtgui_label_3_0 = SNR_ch_2
        self.variable_qtgui_label_3 = variable_qtgui_label_3 = SNR_ch_1
        self.threshold_delta = threshold_delta = 4
        self.su_frame_len = su_frame_len = (su_frame_len_low_rate + len(taps))* 4
        self.rx_gain = rx_gain = .5
        self.pu_frame_len = pu_frame_len = 80*5*9
        self.poll_rate = poll_rate = 10
        self.nfft = nfft = 256
        self.fine_frequency_correction = fine_frequency_correction = 0

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Tab 0')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'waterfall')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'scenario')
        self.top_layout.addWidget(self.tab)
        self._rx_gain_range = Range(0, 1, .05, .5, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RX gain (normalized)', "counter_slider", float)
        self.top_layout.addWidget(self._rx_gain_win)
        self._fine_frequency_correction_range = Range(-10000, 10000, 10, 0, 200)
        self._fine_frequency_correction_win = RangeWidget(self._fine_frequency_correction_range, self.set_fine_frequency_correction, 'Fine frequency correction', "counter_slider", float)
        self.top_layout.addWidget(self._fine_frequency_correction_win)
        self.classifier_energy_detection_vcf_0 = classifier.energy_detection_vcf(nfft, 256, 7)
        self._variable_qtgui_label_3_2_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_3_2_formatter = None
        else:
          self._variable_qtgui_label_3_2_formatter = lambda x: eng_notation.num_to_str(x)

        self._variable_qtgui_label_3_2_tool_bar.addWidget(Qt.QLabel('SNR CH 4 [dB]'+": "))
        self._variable_qtgui_label_3_2_label = Qt.QLabel(str(self._variable_qtgui_label_3_2_formatter(self.variable_qtgui_label_3_2)))
        self._variable_qtgui_label_3_2_tool_bar.addWidget(self._variable_qtgui_label_3_2_label)
        self.tab_layout_0.addWidget(self._variable_qtgui_label_3_2_tool_bar)

        self._variable_qtgui_label_3_1_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_3_1_formatter = None
        else:
          self._variable_qtgui_label_3_1_formatter = lambda x: eng_notation.num_to_str(x)

        self._variable_qtgui_label_3_1_tool_bar.addWidget(Qt.QLabel('SNR CH 3 [dB]'+": "))
        self._variable_qtgui_label_3_1_label = Qt.QLabel(str(self._variable_qtgui_label_3_1_formatter(self.variable_qtgui_label_3_1)))
        self._variable_qtgui_label_3_1_tool_bar.addWidget(self._variable_qtgui_label_3_1_label)
        self.tab_layout_0.addWidget(self._variable_qtgui_label_3_1_tool_bar)

        self._variable_qtgui_label_3_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_3_0_formatter = None
        else:
          self._variable_qtgui_label_3_0_formatter = lambda x: eng_notation.num_to_str(x)

        self._variable_qtgui_label_3_0_tool_bar.addWidget(Qt.QLabel('SNR CH 2 [dB]'+": "))
        self._variable_qtgui_label_3_0_label = Qt.QLabel(str(self._variable_qtgui_label_3_0_formatter(self.variable_qtgui_label_3_0)))
        self._variable_qtgui_label_3_0_tool_bar.addWidget(self._variable_qtgui_label_3_0_label)
        self.tab_layout_0.addWidget(self._variable_qtgui_label_3_0_tool_bar)

        self._variable_qtgui_label_3_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_3_formatter = None
        else:
          self._variable_qtgui_label_3_formatter = lambda x: eng_notation.num_to_str(x)

        self._variable_qtgui_label_3_tool_bar.addWidget(Qt.QLabel('SNR CH 1 [dB]'+": "))
        self._variable_qtgui_label_3_label = Qt.QLabel(str(self._variable_qtgui_label_3_formatter(self.variable_qtgui_label_3)))
        self._variable_qtgui_label_3_tool_bar.addWidget(self._variable_qtgui_label_3_label)
        self.tab_layout_0.addWidget(self._variable_qtgui_label_3_tool_bar)

        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(('type=b200', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_0.set_subdev_spec('A:A', 0)
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(3.195e9+fine_frequency_correction, (3/2)*samp_rate), 0)
        self.uhd_usrp_source_0_0.set_normalized_gain(rx_gain, 0)
        self.uhd_usrp_source_0_0.set_antenna('RX2', 0)
        self.scenario_classification_f = scenario_classification_f.blk(tconst=2, tau1=5, tau2=10, lambda1=20, lambda2=10, lambda3=5)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.5)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	5000, #size
        	samp_rate // nfft, #samp_rate
        	"Averaged power per subchannel", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-50, 20)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.5)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_time_raster_sink_x_0_2 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"Decision Tree",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_2.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_2.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_2.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_2.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_2.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_2_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_raster_sink_x_0_2_win,  1, 0, 1, 1)
        self.qtgui_time_raster_sink_x_0_1_1 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	'Adadelta',
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_1_1.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_1_1.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_1_1.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_1_1.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_1_1.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_1_1.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_1_1_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_1_1.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_raster_sink_x_0_1_1_win, 0, 0, 1, 1)
        self.qtgui_time_raster_sink_x_0_1_0_1 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"Adamax",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_1_0_1.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_1_0_1.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_1_0_1.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_1_0_1.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_1_0_1.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_1_0_1.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_1_0_1_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_1_0_1.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_raster_sink_x_0_1_0_1_win, 0, 1, 1, 1)
        self.qtgui_time_raster_sink_x_0_1_0_0_0_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"previous implementation",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_1_0_0_0_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_1_0_0_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_1_0_0_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_1_0_0_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_1_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_raster_sink_x_0_1_0_0_0_0_win, 2, 0, 1, 3)
        self.qtgui_time_raster_sink_x_0_1_0_0_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"SGD",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_1_0_0_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_1_0_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_1_0_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_1_0_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_raster_sink_x_0_1_0_0_0_win, 0, 2, 1, 1)
        self.qtgui_time_raster_sink_x_0_1_0_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"SGD",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_1_0_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_1_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_1_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_1_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_time_raster_sink_x_0_1_0_0_win, 0, 2, 1, 1)
        self.qtgui_time_raster_sink_x_0_1_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"Adamax",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_1_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_1_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_1_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_1_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_time_raster_sink_x_0_1_0_win, 0, 1, 1, 1)
        self.qtgui_time_raster_sink_x_0_1 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	'Adadelta',
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_1.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_1.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_1.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_1.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_time_raster_sink_x_0_1_win, 0, 0, 1, 1)
        self.qtgui_time_raster_sink_x_0_0_1 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"Knearest",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_0_1.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_0_1.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0_1.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_raster_sink_x_0_0_1_win, 1, 1, 1, 1)
        self.qtgui_time_raster_sink_x_0_0_0_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"SVM",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_0_0_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_0_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._qtgui_time_raster_sink_x_0_0_0_0_win, 1, 2, 1, 1)
        self.qtgui_time_raster_sink_x_0_0_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"SVM",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_0_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_time_raster_sink_x_0_0_0_win, 1, 2, 1, 1)
        self.qtgui_time_raster_sink_x_0_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"Knearest",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_time_raster_sink_x_0_0_win, 1, 1, 1, 1)
        self.qtgui_time_raster_sink_x_0 = qtgui.time_raster_sink_f(
        	samp_rate,
        	100,
        	10,
        	([]),
        	([]),
        	"Decision Tree",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [5, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._qtgui_time_raster_sink_x_0_win,  1, 0, 1, 1)
        self.fft_vxx_1 = fft.fft_vcc(64, True, (window.blackmanharris(64)), True, 4)
        self.fft_vxx_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.classifier_vector_average_vcvc_0 = classifier.vector_average_vcvc(120, 64)
        self.classifier_ml_scn_classification_f_0_0_0 = classifier.ml_scn_classification_f('/home/cuervo/thesis/cognitive_radio_ml/trained_models/sklearn/joblib/svc_full_data_set_rbf_1e6.pkl', True, '/home/cuervo/thesis/cognitive_radio_ml/trained_models/sklearn/joblib/scaler_saved.pkl')
        self.classifier_ml_scn_classification_f_0_0 = classifier.ml_scn_classification_f('/home/cuervo/thesis/cognitive_radio_ml/trained_models/sklearn/joblib/knn_full_data_set_4_neighbors.pkl', False, '/home/cuervo/thesis/cognitive_radio_ml/weights/scaler_saved.pkl')
        self.classifier_ml_scn_classification_f_0 = classifier.ml_scn_classification_f('/home/cuervo/thesis/cognitive_radio_ml/trained_models/sklearn/joblib/dtc_full_data_set_depth_50.pkl', False, '/home/cuervo/thesis/cognitive_radio_ml/weights/scaler_saved.pkl')
        self.classifier_frame_detection_f_0 = classifier.frame_detection_f(su_frame_len/nfft - 9, 5, 5)
        self.classifier_feature_extraction_f_0 = classifier.feature_extraction_f(samp_rate / nfft, 50, pu_frame_len / nfft, 5)
        self.classifier_dl_class_0_0_0 = classifier.dl_class('/home/cuervo/thesis/cognitive_radio_ml/trained_models/keras/checkpoint/sgd_model_checkpoint.h5')
        self.classifier_dl_class_0_0 = classifier.dl_class('/home/cuervo/thesis/cognitive_radio_ml/trained_models/keras/checkpoint/adamax_ckpt.h5')
        self.classifier_dl_class_0 = classifier.dl_class('/home/cuervo/thesis/cognitive_radio_ml/trained_models/keras/checkpoint/new_adadelta_model_checkpoint.h5')
        self.blocks_vector_to_stream_0_3 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_2_1 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_2_0_1 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_2_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_2_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_2_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_2_0 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_2 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_1_0 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_1 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, 10)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 64)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(20, 64, 0)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(64)

        def _SNR_ch_4_probe():
            while True:
                val = self.classifier_energy_detection_vcf_0.get_SNR_4()
                try:
                    self.set_SNR_ch_4(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (poll_rate))
        _SNR_ch_4_thread = threading.Thread(target=_SNR_ch_4_probe)
        _SNR_ch_4_thread.daemon = True
        _SNR_ch_4_thread.start()


        def _SNR_ch_3_probe():
            while True:
                val = self.classifier_energy_detection_vcf_0.get_SNR_3()
                try:
                    self.set_SNR_ch_3(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (poll_rate))
        _SNR_ch_3_thread = threading.Thread(target=_SNR_ch_3_probe)
        _SNR_ch_3_thread.daemon = True
        _SNR_ch_3_thread.start()


        def _SNR_ch_2_probe():
            while True:
                val = self.classifier_energy_detection_vcf_0.get_SNR_2()
                try:
                    self.set_SNR_ch_2(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (poll_rate))
        _SNR_ch_2_thread = threading.Thread(target=_SNR_ch_2_probe)
        _SNR_ch_2_thread.daemon = True
        _SNR_ch_2_thread.start()


        def _SNR_ch_1_probe():
            while True:
                val = self.classifier_energy_detection_vcf_0.get_SNR_1()
                try:
                    self.set_SNR_ch_1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (poll_rate))
        _SNR_ch_1_thread = threading.Thread(target=_SNR_ch_1_probe)
        _SNR_ch_1_thread.daemon = True
        _SNR_ch_1_thread.start()




        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.classifier_vector_average_vcvc_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.fft_vxx_1, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_time_raster_sink_x_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.qtgui_time_raster_sink_x_0_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0, 0), (self.qtgui_time_raster_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_1, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_vector_to_stream_0_1, 0), (self.qtgui_time_raster_sink_x_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_1_0, 0), (self.qtgui_time_raster_sink_x_0_0_1, 0))
        self.connect((self.blocks_vector_to_stream_0_2, 0), (self.qtgui_time_raster_sink_x_0_1, 0))
        self.connect((self.blocks_vector_to_stream_0_2_0, 0), (self.qtgui_time_raster_sink_x_0_1_0, 0))
        self.connect((self.blocks_vector_to_stream_0_2_0_0, 0), (self.qtgui_time_raster_sink_x_0_1_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_2_0_0_0, 0), (self.qtgui_time_raster_sink_x_0_1_0_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_2_0_0_0_0, 0), (self.qtgui_time_raster_sink_x_0_1_0_0_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_2_0_1, 0), (self.qtgui_time_raster_sink_x_0_1_0_1, 0))
        self.connect((self.blocks_vector_to_stream_0_2_1, 0), (self.qtgui_time_raster_sink_x_0_1_1, 0))
        self.connect((self.blocks_vector_to_stream_0_3, 0), (self.qtgui_time_raster_sink_x_0_2, 0))
        self.connect((self.classifier_dl_class_0, 0), (self.blocks_vector_to_stream_0_2, 0))
        self.connect((self.classifier_dl_class_0, 1), (self.blocks_vector_to_stream_0_2_1, 0))
        self.connect((self.classifier_dl_class_0_0, 0), (self.blocks_vector_to_stream_0_2_0, 0))
        self.connect((self.classifier_dl_class_0_0, 1), (self.blocks_vector_to_stream_0_2_0_1, 0))
        self.connect((self.classifier_dl_class_0_0_0, 0), (self.blocks_vector_to_stream_0_2_0_0, 0))
        self.connect((self.classifier_dl_class_0_0_0, 1), (self.blocks_vector_to_stream_0_2_0_0_0, 0))
        self.connect((self.classifier_energy_detection_vcf_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.classifier_energy_detection_vcf_0, 1), (self.blocks_null_sink_1, 1))
        self.connect((self.classifier_energy_detection_vcf_0, 2), (self.blocks_null_sink_1, 2))
        self.connect((self.classifier_energy_detection_vcf_0, 3), (self.blocks_null_sink_1, 3))
        self.connect((self.classifier_energy_detection_vcf_0, 4), (self.classifier_frame_detection_f_0, 0))
        self.connect((self.classifier_energy_detection_vcf_0, 7), (self.classifier_frame_detection_f_0, 1))
        self.connect((self.classifier_energy_detection_vcf_0, 5), (self.classifier_frame_detection_f_0, 2))
        self.connect((self.classifier_energy_detection_vcf_0, 6), (self.classifier_frame_detection_f_0, 3))
        self.connect((self.classifier_energy_detection_vcf_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.classifier_energy_detection_vcf_0, 1), (self.qtgui_time_sink_x_0_0_0_0, 1))
        self.connect((self.classifier_energy_detection_vcf_0, 2), (self.qtgui_time_sink_x_0_0_0_0, 2))
        self.connect((self.classifier_energy_detection_vcf_0, 3), (self.qtgui_time_sink_x_0_0_0_0, 3))
        self.connect((self.classifier_feature_extraction_f_0, 0), (self.classifier_ml_scn_classification_f_0, 0))
        self.connect((self.classifier_feature_extraction_f_0, 1), (self.classifier_ml_scn_classification_f_0, 1))
        self.connect((self.classifier_feature_extraction_f_0, 2), (self.classifier_ml_scn_classification_f_0, 2))
        self.connect((self.classifier_feature_extraction_f_0, 3), (self.classifier_ml_scn_classification_f_0, 3))
        self.connect((self.classifier_feature_extraction_f_0, 4), (self.classifier_ml_scn_classification_f_0, 4))
        self.connect((self.classifier_feature_extraction_f_0, 5), (self.classifier_ml_scn_classification_f_0, 5))
        self.connect((self.classifier_feature_extraction_f_0, 0), (self.classifier_ml_scn_classification_f_0_0, 0))
        self.connect((self.classifier_feature_extraction_f_0, 1), (self.classifier_ml_scn_classification_f_0_0, 1))
        self.connect((self.classifier_feature_extraction_f_0, 2), (self.classifier_ml_scn_classification_f_0_0, 2))
        self.connect((self.classifier_feature_extraction_f_0, 3), (self.classifier_ml_scn_classification_f_0_0, 3))
        self.connect((self.classifier_feature_extraction_f_0, 4), (self.classifier_ml_scn_classification_f_0_0, 4))
        self.connect((self.classifier_feature_extraction_f_0, 5), (self.classifier_ml_scn_classification_f_0_0, 5))
        self.connect((self.classifier_feature_extraction_f_0, 0), (self.classifier_ml_scn_classification_f_0_0_0, 0))
        self.connect((self.classifier_feature_extraction_f_0, 1), (self.classifier_ml_scn_classification_f_0_0_0, 1))
        self.connect((self.classifier_feature_extraction_f_0, 2), (self.classifier_ml_scn_classification_f_0_0_0, 2))
        self.connect((self.classifier_feature_extraction_f_0, 3), (self.classifier_ml_scn_classification_f_0_0_0, 3))
        self.connect((self.classifier_feature_extraction_f_0, 4), (self.classifier_ml_scn_classification_f_0_0_0, 4))
        self.connect((self.classifier_feature_extraction_f_0, 5), (self.classifier_ml_scn_classification_f_0_0_0, 5))
        self.connect((self.classifier_feature_extraction_f_0, 0), (self.scenario_classification_f, 0))
        self.connect((self.classifier_feature_extraction_f_0, 1), (self.scenario_classification_f, 1))
        self.connect((self.classifier_feature_extraction_f_0, 2), (self.scenario_classification_f, 2))
        self.connect((self.classifier_feature_extraction_f_0, 3), (self.scenario_classification_f, 3))
        self.connect((self.classifier_feature_extraction_f_0, 4), (self.scenario_classification_f, 4))
        self.connect((self.classifier_feature_extraction_f_0, 5), (self.scenario_classification_f, 5))
        self.connect((self.classifier_frame_detection_f_0, 0), (self.classifier_feature_extraction_f_0, 0))
        self.connect((self.classifier_frame_detection_f_0, 1), (self.classifier_feature_extraction_f_0, 1))
        self.connect((self.classifier_ml_scn_classification_f_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.classifier_ml_scn_classification_f_0, 1), (self.blocks_vector_to_stream_0_3, 0))
        self.connect((self.classifier_ml_scn_classification_f_0_0, 0), (self.blocks_vector_to_stream_0_1, 0))
        self.connect((self.classifier_ml_scn_classification_f_0_0, 1), (self.blocks_vector_to_stream_0_1_0, 0))
        self.connect((self.classifier_ml_scn_classification_f_0_0_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.classifier_ml_scn_classification_f_0_0_0, 1), (self.blocks_vector_to_stream_0_0_0, 0))
        self.connect((self.classifier_vector_average_vcvc_0, 0), (self.classifier_dl_class_0, 0))
        self.connect((self.classifier_vector_average_vcvc_0, 0), (self.classifier_dl_class_0_0, 0))
        self.connect((self.classifier_vector_average_vcvc_0, 0), (self.classifier_dl_class_0_0_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.classifier_energy_detection_vcf_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.scenario_classification_f, 0), (self.blocks_vector_to_stream_0_2_0_0_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "scenario_classification_ml")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_subchan_map(self):
        return self.subchan_map

    def set_subchan_map(self, subchan_map):
        self.subchan_map = subchan_map

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(3.195e9+self.fine_frequency_correction, (3/2)*self.samp_rate), 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.samp_rate // self.nfft)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_packetlen_base(self):
        return self.packetlen_base

    def set_packetlen_base(self, packetlen_base):
        self.packetlen_base = packetlen_base

    def get_cfg(self):
        return self.cfg

    def set_cfg(self, cfg):
        self.cfg = cfg

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.set_su_frame_len((self.su_frame_len_low_rate + len(self.taps))* 4)

    def get_phydyas_taps_time(self):
        return self.phydyas_taps_time

    def set_phydyas_taps_time(self, phydyas_taps_time):
        self.phydyas_taps_time = phydyas_taps_time

    def get_nguard_bins(self):
        return self.nguard_bins

    def set_nguard_bins(self, nguard_bins):
        self.nguard_bins = nguard_bins

    def get_nchan(self):
        return self.nchan

    def set_nchan(self, nchan):
        self.nchan = nchan

    def get_sync(self):
        return self.sync

    def set_sync(self, sync):
        self.sync = sync

    def get_su_frame_len_low_rate(self):
        return self.su_frame_len_low_rate

    def set_su_frame_len_low_rate(self, su_frame_len_low_rate):
        self.su_frame_len_low_rate = su_frame_len_low_rate
        self.set_su_frame_len((self.su_frame_len_low_rate + len(self.taps))* 4)

    def get_SNR_ch_4(self):
        return self.SNR_ch_4

    def set_SNR_ch_4(self, SNR_ch_4):
        self.SNR_ch_4 = SNR_ch_4
        self.set_variable_qtgui_label_3_2(self._variable_qtgui_label_3_2_formatter(self.SNR_ch_4))

    def get_SNR_ch_3(self):
        return self.SNR_ch_3

    def set_SNR_ch_3(self, SNR_ch_3):
        self.SNR_ch_3 = SNR_ch_3
        self.set_variable_qtgui_label_3_1(self._variable_qtgui_label_3_1_formatter(self.SNR_ch_3))

    def get_SNR_ch_2(self):
        return self.SNR_ch_2

    def set_SNR_ch_2(self, SNR_ch_2):
        self.SNR_ch_2 = SNR_ch_2
        self.set_variable_qtgui_label_3_0(self._variable_qtgui_label_3_0_formatter(self.SNR_ch_2))

    def get_SNR_ch_1(self):
        return self.SNR_ch_1

    def set_SNR_ch_1(self, SNR_ch_1):
        self.SNR_ch_1 = SNR_ch_1
        self.set_variable_qtgui_label_3(self._variable_qtgui_label_3_formatter(self.SNR_ch_1))

    def get_variable_qtgui_label_3_2(self):
        return self.variable_qtgui_label_3_2

    def set_variable_qtgui_label_3_2(self, variable_qtgui_label_3_2):
        self.variable_qtgui_label_3_2 = variable_qtgui_label_3_2
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_3_2_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_3_2))

    def get_variable_qtgui_label_3_1(self):
        return self.variable_qtgui_label_3_1

    def set_variable_qtgui_label_3_1(self, variable_qtgui_label_3_1):
        self.variable_qtgui_label_3_1 = variable_qtgui_label_3_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_3_1_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_3_1))

    def get_variable_qtgui_label_3_0(self):
        return self.variable_qtgui_label_3_0

    def set_variable_qtgui_label_3_0(self, variable_qtgui_label_3_0):
        self.variable_qtgui_label_3_0 = variable_qtgui_label_3_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_3_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_3_0))

    def get_variable_qtgui_label_3(self):
        return self.variable_qtgui_label_3

    def set_variable_qtgui_label_3(self, variable_qtgui_label_3):
        self.variable_qtgui_label_3 = variable_qtgui_label_3
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_3_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_3))

    def get_threshold_delta(self):
        return self.threshold_delta

    def set_threshold_delta(self, threshold_delta):
        self.threshold_delta = threshold_delta

    def get_su_frame_len(self):
        return self.su_frame_len

    def set_su_frame_len(self, su_frame_len):
        self.su_frame_len = su_frame_len

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0_0.set_normalized_gain(self.rx_gain, 0)


    def get_pu_frame_len(self):
        return self.pu_frame_len

    def set_pu_frame_len(self, pu_frame_len):
        self.pu_frame_len = pu_frame_len

    def get_poll_rate(self):
        return self.poll_rate

    def set_poll_rate(self, poll_rate):
        self.poll_rate = poll_rate

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.samp_rate // self.nfft)

    def get_fine_frequency_correction(self):
        return self.fine_frequency_correction

    def set_fine_frequency_correction(self, fine_frequency_correction):
        self.fine_frequency_correction = fine_frequency_correction
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(3.195e9+self.fine_frequency_correction, (3/2)*self.samp_rate), 0)


def main(top_block_cls=scenario_classification_ml, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
