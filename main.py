import multiprocessing
import psutil
import configargparse

def configuration_parsing(t_config_parser):
    # Use a breakpoint in the code line below to debug your script.
    # p.add("-m2a", '--Enable_Mf42Asc', action="store_true", help="Synchronize radar and merged video data")
    # p.add("-m2a_e", '--Mf42Asc_executable_path', type=str, help="executable path for ASM2MF4")
    # p.add("-m2a_c", '--Mf42Asc_channel_name', type=str, help="channel name which will be trasmited")
    # p.add("-m2a_m", '--Mf42Asc_Mf4_path', type=str, help="Path for storing the converted ASC")
    # p.add("-m2a_a", '--Mf42Asc_Asc_path', type=str, help="Path for storing MF4 need to convert")
    # p.add("-a2m", '--Enable_Asc2Mf4', action="store_true", help="Asc to MF4 convert will run")
    # p.add("-a2m_a_p", '--Asc2Mf4_Asc_path', type=str, help="Path for storing asc need to convert")
    # p.add("-a2m_m", '--Asc2Mf4_Mf4_path', type=str, help="Path for storing the converted mf4")
    # p.add("-a2m_e", '--Asc2Mf4_executable_path', type=str, help="executable path for ASM2MF4")
    # p.add("-a2m_d", '--Asc2Mf4_dll_path', type=str, help="DLL path for ASM2MF4")
    # p.add("-a2m_c", '--Asc2Mf4_canape_config_path', type=str, help="ini path for ASM2MF4")
    # p.add("-i", '--Radar_file_path', required=True, type=str, help="Full path of ER radar data root folder")
    # p.add("-s", '--Enable_Sync_video', action="store_true", help="Synchronize radar and merged video data")
    # p.add("-so", '--RV_Sync_Video_output_path', type=str, help="Output path for synchronized video file")
    # p.add("-m", '--Enable_Merge_video', action="store_true", help="Merge video data")
    # p.add("-mm_o", '--Mf4Merger_output_path', type=str, help="Output path for merged video file")
    # p.add("-e", '--Enable_Excel_output', action="store_true",
    #       help="Collect data information in an excel and output to top folder")
    # p.add("-p", '--Enable_Playlist_output', action="store_true", help="Enable play list output")
    # p.add("-pp", '--Playlist_path', type=str, help="Output path of playlist")
    # p.add("-mt", '--Enable_Multiprocessing', action="store_true", help="using multi threading to collect information")
    print("ErToolChain START")
    print("Please check the configuration !!!")
    print(t_config_parser.format_values())
    start = input('Continue? (if not, ctrl + c)')
    return t_config_parser.parse_args()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    core_no = multiprocessing.cpu_count()
    mem = psutil.virtual_memory()
    mem1 = str(mem.total / 1024 / 1024 / 1024)
    net = psutil.net_if_stats()

    parser = configargparse.ArgParser(default_config_files=['./config.ini'])
    configuration_parsing(parser)
