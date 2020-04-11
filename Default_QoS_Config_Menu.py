#!/usr/bin/env python2
"""
Created: April 8, 2020
@Author: Reynaldo Abreu
Version: 1.2
Modified: April 10, 2020
"""

#Variables
MTU_size = 1500
worth_buffered_data = 0.05
byte_to_bits = 8
def lnbreak ():
    print("\n")

def lnexit ():
    print ("exit\n")

def Oops():
    print ("-----------------------------------------------------------")
    print ("     Oops Invalid choice. Enter a valid choice number!     ")
    print ("-----------------------------------------------------------")

# Create the QoS_6Q_P1
def QOS_6Q_P1():
    a_total_bw = int (input ('Enter the Total Bandwidth Subscribe: '))
    lnbreak()
    a_voice_dscp = int (input ('Voice Class percent: '))
    a_network_control_dscp = int (input ('Network Control Class percent: '))
    a_interactive_video_dscp = int (input ('Interactive Video Class percent: '))
    a_streaming_video_dscp = int (input ('Streaming Video Class percent: '))
    a_call_signaling_dscp = int (input ('Signaling Class percent: '))
    a_critical_data_dscp = int (input ('Critical Data Class percent: '))
    a_scavenger_dscp = int  (input ('Scavenger Class percent: '))
    a_class_default = int (input ('Class-Default percent: '))
    a_qos_pkt = int (round ((((a_total_bw) / (byte_to_bits)) * (worth_buffered_data)) / (MTU_size) * 1000000,0))
    a_total_percentage = a_network_control_dscp+a_interactive_video_dscp+a_streaming_video_dscp+a_call_signaling_dscp+a_critical_data_dscp+a_scavenger_dscp+a_class_default
    lnbreak()
       
    if a_total_percentage < 100:
        print ("------------------------------------------------------------")
        print ("   Oops! Total Bandwidht Remaining needs to be 100% Total   ")
        print ("                      Let's try Again!                      ")
        print ("------------------------------------------------------------")
        lnbreak()
        print ("--------------------------------------------------------------------------------------------------------")
        print ("      You are missing: ", 100 - (a_total_percentage),"% bandwidth that needs to be added to a class.      ")
        print ("--------------------------------------------------------------------------------------------------------")
        lnbreak()
        mainMenu()

    else:
        print ("------------------------------------------------------------")
        print("          Copy and Paste this config into the router         ")
        print ("------------------------------------------------------------")
        lnbreak()
        print("configuration terminal")
        print(f'policy-map QOS_6Q_P1 \n class VOICE_DSCP-WAN\n priority level 1\n police cir percent {a_voice_dscp}\n set dscp ef')
        print(f'class NETWORK_CONTROL-DSCP\n bandwidth remaining percent {a_network_control_dscp}\n set dscp cs6')
        print(f'class INTERACTIVE_VIDEO-WAN\n bandwidth remaining percent {a_interactive_video_dscp}\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp af41')
        print(f'class STREAMING_VIDEO-WAN\n bandwidth remaining percent {a_streaming_video_dscp}\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp af31')
        print(f'class CALL_SIGNALING-WAN\n bandwidth remaining percent {a_call_signaling_dscp}\n set dscp af21')
        print(f'class CRITICAL_DATA-WAN\n bandwidth remaining percent {a_critical_data_dscp}\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp af21')
        print(f'class SCAVENGER-WAN\n bandwidth remaining percent {a_scavenger_dscp}\n set dscp af11')
        print(f'class class-default\n bandwidth remaining percent {a_class_default}\n queue-limit {a_qos_pkt}\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp default')
        lnbreak()
        print ("------------------------------------------------------------")
        print ("                  Returning to Main Menu                    ")
        print ("------------------------------------------------------------")
        mainMenu()

# Create the QoS_6Q_P3
def QOS_8Q_P3():
    """
    print ("-----------------------------------------------------------")
    b_total_bw = int (input ('           Enter the Total Bandwidth Subscribe: '))
    print ("-----------------------------------------------------------")
    """
    b_voice_dscp = int (input ('Voice Class percent: '))
    b_broadcast_video_dscp = int (input ('Broadcast Video Class percent: '))
    b_interactive_video_dscp = int (input ('Real Interactive Video Class percent: '))
    b_network_control_dscp = int (input ('Network Control Class percent: '))
    b_call_signaling_dscp = int (input ('Signaling Class percent: '))
    b_network_mgmtl_dscp = int (input ('Network Management Class percent: '))
    b_multimedia_conf_dscp = int (input ('Multimedia Conferencing Class percent: '))
    b_multimedia_stream_dscp = int (input ('Multimedia Streaming Class percent: '))
    b_transaction_dscp = int (input ('Transactional Data Class percent: '))
    b_bulk_data_dscp = int (input ('Bulk Data Class percent: '))
    b_scavenger_dscp = int  (input ('Scavenger Class percent: '))
    b_class_default = int (input ('Class-Default percent: '))
    #b_qos_pkt = int (round ((((b_total_bw) / (byte_to_bits)) * (worth_buffered_data)) / (MTU_size) * 1000000,0))
    b_total_percentage = b_voice_dscp+b_broadcast_video_dscp+b_interactive_video_dscp+b_network_control_dscp+b_call_signaling_dscp+b_network_mgmtl_dscp+b_multimedia_conf_dscp+b_multimedia_stream_dscp+b_transaction_dscp+b_bulk_data_dscp+b_scavenger_dscp+b_class_default
    lnbreak()

    if b_total_percentage < 100:
        print ("------------------------------------------------------------")
        print ("   Oops! Total Bandwidht Remaining needs to be 100% Total   ")
        print ("                      Let's try Again!                      ")
        print ("------------------------------------------------------------")
        lnbreak()
        print ("--------------------------------------------------------------------------------------------------------")
        print ("      You are missing: ", 100 - (b_total_percentage),"% bandwidth that needs to be added to a class.      ")
        print ("--------------------------------------------------------------------------------------------------------")
        lnbreak()
        mainMenu()

    else:
        print ("------------------------------------------------------------")
        print("          Copy and Paste this config into the router         ")
        print ("------------------------------------------------------------")
        lnbreak()
        print("configuration terminal")
        print (f'policy-map QOS_8Q_P3\n class VOICE-DSCP\n priority percent {b_voice_dscp}')
        print (f'class BROADCAST_VIDEO-DSCP\n priority percent {b_broadcast_video_dscp}')
        print (f'class REALTIME_INTERACTIVE-DSCP\n priority percent {b_interactive_video_dscp}')
        print (f'class NETWORK_CONTROL-DSCP\n bandwidth remaining percent {b_network_control_dscp}')
        print (f'class SIGNALING-DSCP\n bandwidth remaining percent {b_call_signaling_dscp}')
        print (f'class NETWORK_MANAGEMENT-DSCP\n bandwidth remaining percent {b_network_mgmtl_dscp}')
        print (f'class MULTIMEDIA_CONFERENCING-DSCP\n bandwidth remaining percent {b_multimedia_conf_dscp}\n fair-queue\n random-detect dscp-based')
        print (f'class MULTIMEDIA_STREAMING-DSCP\n bandwidth remaining percent {b_multimedia_stream_dscp}\n fair-queue\n random-detect dscp-based')
        print (f'class TRANSACTIONAL_DATA-DSCP\n bandwidth  remaining percent {b_transaction_dscp}\n fair-queue\n random-detect dscp-based')
        print (f'class BULK_DATA-DSCP\n bandwidth remaining percent {b_bulk_data_dscp}\n fair-queue\n random-detect dscp-based')
        print (f'class SCAVENGER-DSCP\n bandwidth remaining percent {b_scavenger_dscp}')
        print (f'class class-default\n bandwidth remaining percent {b_class_default}\n fair-queue\n random-detect dscp-based')
        lnbreak()
        print ("------------------------------------------------------------")
        print ("                  Returning to Main Menu                    ")
        print ("------------------------------------------------------------")
        mainMenu()

# Generate the Default QoS_6Q_P1
def QOS_6Q_P1_DEF():
    print ("------------------------------------------------------------")
    print("          Copy and Paste this config into the router         ")
    print ("------------------------------------------------------------")
    lnbreak()
    print("configuration terminal")
    print(f'policy-map QOS_6Q_P1 \n class VOICE_DSCP-WAN\n priority level 1\n police cir percent 10\n set dscp ef')
    print(f'class NETWORK_CONTROL-DSCP\n bandwidth remaining percent 5\n set dscp cs6')
    print(f'class INTERACTIVE_VIDEO-WAN\n bandwidth remaining percent 30\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp af41')
    print(f'class STREAMING_VIDEO-WAN\n bandwidth remaining percent 10\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp af31')
    print(f'class CALL_SIGNALING-WAN\n bandwidth remaining percent 4\n set dscp af21')
    print(f'class CRITICAL_DATA-WAN\n bandwidth remaining percent 25\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp af21')
    print(f'class SCAVENGER-WAN\n bandwidth remaining percent 1\n set dscp af11')
    print(f'class class-default\n bandwidth remaining percent 25\n queue-limit 512\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp default')
    lnbreak()
    print ("------------------------------------------------------------")
    print ("                  Returning to Main Menu                    ")
    print ("------------------------------------------------------------")
    mainMenu()

# Generate the Default QoS_8Q_P3
def QOS_8Q_P3_DEF():

    print ("------------------------------------------------------------")
    print("          Copy and Paste this config into the router         ")
    print ("------------------------------------------------------------")
    lnbreak()
    print("configuration terminal")
    print (f'policy-map QOS_8Q_P3\n class VOICE-DSCP\n priority percent 10')
    print (f'class BROADCAST_VIDEO-DSCP\n priority percent 10')
    print (f'class REALTIME_INTERACTIVE-DSCP\n priority percent 13')
    print (f'class NETWORK_CONTROL-DSCP\n bandwidth remaining percent 2')
    print (f'class SIGNALING-DSCP\n bandwidth remaining percent 2')
    print (f'class NETWORK_MANAGEMENT-DSCP\n bandwidth remaining percent 3')
    print (f'class MULTIMEDIA_CONFERENCING-DSCP\n bandwidth remaining percent 10\n fair-queue\n random-detect dscp-based')
    print (f'class MULTIMEDIA_STREAMING-DSCP\n bandwidth remaining percent 10\n fair-queue\n random-detect dscp-based')
    print (f'class TRANSACTIONAL_DATA-DSCP\n bandwidth  remaining percent 10\n fair-queue\n random-detect dscp-based')
    print (f'class BULK_DATA-DSCP\n bandwidth remaining percent 4\n fair-queue\n random-detect dscp-based')
    print (f'class SCAVENGER-DSCP\n bandwidth remaining percent 1')
    print (f'class class-default\n bandwidth remaining percent 25\n fair-queue\n random-detect dscp-based')
    lnbreak()
    print ("------------------------------------------------------------")
    print ("                  Returning to Main Menu                    ")
    print ("------------------------------------------------------------")
    mainMenu()
    

#Generate QoS for Tunnel DMVPN Connections
def tunnel_WAN():
    """
    c_total_bw = int (input ('Enter the Total Bandwidth Subscribe: '))
    """
    lnbreak()
    c_video = int (input ('Voice Class percent: '))
    c_net_ctrl_mgmt = int (input ('Network Control MGMT Class percent: '))
    c_int_video = int (input ('Interactive Video Class percent: '))
    c_broad_video = int (input ('Broadcasting Video Class percent: '))
    c_signaling = int (input ('Signaling Class percent: '))
    c_data = int (input ('Critical Data Class percent: '))
    c_scavenger = int  (input ('Scavenger Class percent: '))
    c_class_default = int (input ('Class-Default percent: '))
    c_total_percentage = c_net_ctrl_mgmt+c_int_video+c_broad_video+c_signaling+c_data+c_scavenger+c_class_default
    lnbreak()

    if c_total_percentage < 100:
        print ("------------------------------------------------------------")
        print ("   Oops! Total Bandwidht Remaining needs to be 100% Total   ")
        print ("                      Let's try Again!                      ")
        print ("------------------------------------------------------------")
        lnbreak()
        print ("--------------------------------------------------------------------------------------------------------")
        print ("      You are missing: ", 100 - (c_total_percentage),"% bandwidth that needs to be added to a class.      ")
        print ("--------------------------------------------------------------------------------------------------------")
        lnbreak()
        mainMenu()

    else:
        print ("------------------------------------------------------------")
        print("          Copy and Paste this config into the router         ")
        print ("------------------------------------------------------------")
        lnbreak()
        print("configuration terminal")
        print (f'policy-map WAN\n class VOICE\n priority level 1\n policy cir percent {c_video}\n set dscp tunnel ef')
        print (f'class STREAMING-VIDEO\n bandwidth remaining percent {c_broad_video}\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp tunnel af31')
        print (f'class INTERACTIVE-VIDEO\n bandwidth remaining percent {c_int_video}\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp tunnel af41')
        print (f'class NET-CTRL-MGMT\n bandwidth remaining percent {c_net_ctrl_mgmt}\n set dscp tunnel cs6')
        print (f'class CALL-SIGNALING\n bandwidth remaining percent {c_signaling}\n set dscp tunnel af21')
        print (f'class CRITICAL-DATA\n bandwidth remaining percent {c_data}\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp tunnel af21')
        print (f'class SCAVENGER-DSCP\n bandwidth remaining percent {c_scavenger}\n set dscp tunnel af11')
        print (f'class class-default\n bandwidth remaining percent {c_class_default}\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp tunnel default')
        lnbreak()
        print ("------------------------------------------------------------")
        print ("                  Returning to Main Menu                    ")
        print ("------------------------------------------------------------")
        mainMenu()

#Generate the Default Tunnel WAN QoS
def tunnel_WAN_DEF():
    print ("------------------------------------------------------------")
    print("          Copy and Paste this config into the router         ")
    print ("------------------------------------------------------------")
    lnbreak()
    print("configuration terminal")
    print (f'policy-map WAN\n class VOICE\n priority level 1\n policy cir percent 10\n set dscp tunnel ef')
    print (f'class STREAMING-VIDEO\n bandwidth remaining percent 10\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp tunnel af31')
    print (f'class INTERACTIVE-VIDEO\n bandwidth remaining percent 30\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp tunnel af41')
    print (f'class NET-CTRL-MGMT\n bandwidth remaining percent 5\n set dscp tunnel cs6')
    print (f'class CALL-SIGNALING\n bandwidth remaining percent 4\n set dscp tunnel af21')
    print (f'class CRITICAL-DATA\n bandwidth remaining percent 25\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp tunnel af21')
    print (f'class SCAVENGER-DSCP\n bandwidth remaining percent 1\n set dscp tunnel af11')
    print (f'class class-default\n bandwidth remaining percent 25\n random-detect dscp-based\n random-detect exponential-weighting-constant 9\n set dscp tunnel default')
    lnbreak()
    mainMenu()

#Display the Menu Options
def mainMenu():
    print ("1 | Build QoS_6Q_P1")
    print ("2 | Build QoS_8Q_P3")
    print ("3 | Build QoS_WAN for DMVPN Connections")
    print ("4 | Default QoS_6Q_P1 Configuration")
    print ("5 | Default QoS_8Q_P3 Configuration")
    print ("6 | Default QoS_WAN DMVPN Configuration")
    print ("9 | Quit")
    while True:
        try:
            selection = int (input ("Please Enter choice: "))
            if selection == 1:
                QOS_6Q_P1()
                break

            elif selection == 2:
                QOS_8Q_P3()
                break

            elif selection == 3:
                tunnel_WAN()
                break

            elif selection == 4:
                QOS_6Q_P1_DEF()
                break

            elif selection == 5:
                QOS_8Q_P3_DEF()
                break

            elif selection == 6:
                tunnel_WAN_DEF()
                break

            elif selection == 9:
                print ("---------------------------")
                print ("         GOOD BYE!         ")
                print ("---------------------------")
                lnbreak()
                break
            
            else:
                lnbreak()
                Oops()
                lnbreak()
                mainMenu()
        except ValueError:
            lnbreak()
            Oops()
            lnbreak()
    exit

#Display mainMenu
mainMenu()