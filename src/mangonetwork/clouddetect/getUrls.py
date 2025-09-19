def getURL():

    #x means reviewed and approved as of sept 22
    urls = [['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/156/07/mango-low-greenline-20220605-071400.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/061/02/mango-low-greenline-20240301-025400.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/210/04/mango-low-greenline-20240728-043200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/326/03/mango-low-greenline-20221122-030600.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/128/07/mango-low-greenline-20220508-072600.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/133/10/mango-low-greenline-20220513-104600.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/213/06/mango-low-greenline-20240731-060200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/137/04/mango-low-greenline-20220517-043800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/139/04/mango-low-greenline-20220519-040600.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/147/04/mango-low-greenline-20220527-041400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/149/10/mango-low-greenline-20220529-103000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/151/04/mango-low-greenline-20220531-042400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/158/06/mango-low-greenline-20220607-065800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/166/04/mango-low-greenline-20220615-042800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/167/05/mango-low-greenline-20220616-050000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/071/09/mango-low-greenline-20220312-091400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/073/12/mango-low-greenline-20220314-120000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/074/12/mango-low-greenline-20220315-120000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/037/07/mango-low-greenline-20220206-070000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/038/05/mango-low-greenline-20220207-053400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/039/10/mango-low-greenline-20220208-100000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/040/10/mango-low-greenline-20220209-100000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/041/12/mango-low-greenline-20220210-121800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/042/09/mango-low-greenline-20220211-093400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/043/12/mango-low-greenline-20220212-122600.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/044/12/mango-low-greenline-20220213-123400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/029/07/mango-low-greenline-20220129-072800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/333/10/mango-low-greenline-20221129-101200.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/214/07/mango-low-greenline-20240801-071200.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/296/02/mango-low-greenline-20221023-023200.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/217/04/mango-low-greenline-20240804-044800.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/222/07/mango-low-greenline-20240809-075800.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/248/07/mango-low-greenline-20240904-070200.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/081/03/mango-low-greenline-20220322-030400.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/251/11/mango-low-greenline-20240907-113600.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/180/05/mango-low-greenline-20240628-052400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/099/03/mango-low-greenline-20240408-032800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/051/04/mango-low-greenline-20220220-040600.hdf5', 'Y'], #this was wrong label (is clear)
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/052/02/mango-low-greenline-20220221-024200.hdf5', 'Y'], #this was wrong label  (is clear)
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/116/09/mango-low-greenline-20220426-095600.hdf5', 'Y'], #37, this was wrong label

    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/054/10/mango-low-greenline-20220223-104000.hdf5', 'N'], #this looks weird and maybe has moon interference
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/034/12/mango-low-greenline-20220203-122600.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/319/05/mango-low-greenline-20231115-055800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/309/03/mango-low-greenline-20231105-031600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/028/02/mango-low-greenline-20220128-024200.hdf5', 'Y'], #wrongly labelled as cloudy 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/282/03/mango-low-greenline-20231009-030200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/259/03/mango-low-greenline-20230916-032800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/362/04/mango-low-greenline-20221228-040600.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/254/04/mango-low-greenline-20230911-045000.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/331/04/mango-low-greenline-20221127-043400.hdf5', 'N'], #maybe go earlier in the day on this? pretty close to ok
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2022/328/03/mango-low-greenline-20221124-031400.hdf5', 'Y'], #x
  #what
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/231/04/mango-low-greenline-20230819-043400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/229/04/mango-low-greenline-20230817-040400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/227/04/mango-low-greenline-20230815-040200.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/223/05/mango-low-greenline-20230811-053800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/204/07/mango-low-greenline-20230723-074200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/193/06/mango-low-greenline-20230712-061600.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/204/09/mango-blo-greenline-20220723-094000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/168/05/mango-low-greenline-20230617-050600.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/136/04/mango-low-greenline-20230516-042800.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/189/05/mango-low-greenline-20230708-054000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/079/04/mango-low-greenline-20230320-040000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/074/03/mango-low-greenline-20230315-032600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/172/05/mango-low-greenline-20230621-050800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/148/07/mango-blo-greenline-20220528-072600.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/245/11/mango-low-greenline-20240901-112800.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2024/252/03/mango-low-greenline-20240908-032400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/187/05/mango-low-greenline-20230706-054400.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/112/04/mango-low-greenline-20230422-041800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/low/greenline/raw/2023/106/03/mango-low-greenline-20230416-035800.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/236/06/mango-blo-greenline-20220824-062600.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/243/07/mango-blo-greenline-20220831-074000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/273/04/mango-blo-greenline-20240929-045000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/250/07/mango-blo-greenline-20240906-073600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/246/06/mango-blo-greenline-20240902-060200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/239/04/mango-blo-greenline-20240826-040800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/246/05/mango-blo-greenline-20220903-053800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/293/07/mango-blo-greenline-20221020-072800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/220/04/mango-blo-greenline-20240807-044600.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/305/05/mango-blo-greenline-20221101-050400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/291/04/mango-blo-greenline-20221018-043800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/292/05/mango-blo-greenline-20221019-051000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/213/06/mango-blo-greenline-20240731-060000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/187/06/mango-blo-greenline-20240705-063800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/183/05/mango-blo-greenline-20240701-055800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/288/04/mango-blo-greenline-20221015-040400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/158/06/mango-blo-greenline-20240606-062400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/268/08/mango-blo-greenline-20220925-083000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/271/07/mango-blo-greenline-20220928-073200.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/100/09/mango-blo-greenline-20240409-093000.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/042/03/mango-blo-greenline-20240211-031400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/260/03/mango-blo-greenline-20230917-033000.hdf5', 'Y'],
    #https://www.mangonetwork.org/mango/v1/database/sites/bdr/greenline/2024-08-27 bird on the camera LOL
    #BDR Data
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2022/359/03/mango-bdr-greenline-20221225-031400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/291/04/mango-bdr-greenline-20231018-045000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/071/04/mango-bdr-greenline-20230312-040600.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/288/01/mango-bdr-greenline-20231015-014600.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/091/09/mango-bdr-greenline-20230401-094200.hdf5', 'Y'], #x check again later
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/254/02/mango-bdr-greenline-20230911-023000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/252/02/mango-bdr-greenline-20230909-024400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/017/04/mango-bdr-greenline-20230117-041000.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/026/08/mango-bdr-greenline-20230126-084800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/151/09/mango-bdr-greenline-20230531-091200.hdf5', 'Y'], #x but close 
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/177/08/mango-bdr-greenline-20230626-085800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/166/07/mango-bdr-greenline-20230615-074200.hdf5', 'Y'], #x but close   100
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/121/09/mango-bdr-greenline-20230501-093400.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/015/07/mango-bdr-greenline-20230115-072800.hdf5', 'Y'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/042/03/mango-bdr-greenline-20230211-034400.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/086/08/mango-bdr-greenline-20230327-080600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/028/03/mango-bdr-greenline-20230128-034000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/043/07/mango-bdr-greenline-20230212-072400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/048/05/mango-bdr-greenline-20230217-053800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/051/05/mango-bdr-greenline-20230220-054200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/059/07/mango-bdr-greenline-20230228-072400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/119/09/mango-bdr-greenline-20230429-094200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/107/04/mango-bdr-greenline-20230417-043800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/103/05/mango-bdr-greenline-20230413-053400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/070/03/mango-bdr-greenline-20230311-034200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/022/04/mango-bdr-greenline-20230122-044800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/004/11/mango-bdr-greenline-20230104-114000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/095/10/mango-bdr-greenline-20230405-103200.hdf5', 'N'], #x this day is very cool, thunderstorm
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/105/06/mango-bdr-greenline-20230415-063600.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/077/07/mango-bdr-greenline-20230318-073600.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/077/11/mango-bdr-greenline-20230318-110000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/114/05/mango-bdr-greenline-20230424-053600.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/028/09/mango-bdr-greenline-20230128-094200.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/045/04/mango-bdr-greenline-20230214-043400.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/113/07/mango-bdr-greenline-20230423-073400.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2024/117/03/mango-bdr-greenline-20240426-031800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2022/347/05/mango-bdr-greenline-20221213-051200.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/082/05/mango-bdr-greenline-20230323-052200.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/284/02/mango-bdr-greenline-20231011-021200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/132/05/mango-bdr-greenline-20230512-054000.hdf5', 'N'], #x get one from the 14th of this month, big storm
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/141/10/mango-bdr-greenline-20230521-100000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2022/338/11/mango-bdr-greenline-20221204-113800.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/089/08/mango-bdr-greenline-20230330-084800.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/280/06/mango-bdr-greenline-20231007-062600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/002/08/mango-bdr-greenline-20230102-085400.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/024/04/mango-bdr-greenline-20230124-045400.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/258/02/mango-bdr-greenline-20230915-025400.hdf5', 'N'],

#https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2023/095/10/ really cool hour of lightning

    #CFS DATA
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/105/09/mango-cfs-greenline-20230415-091200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/131/07/mango-cfs-greenline-20230511-072800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/131/09/mango-cfs-greenline-20230511-090600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/201/09/mango-cfs-greenline-20230720-091000.hdf5', 'Y'], #140
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/189/05/mango-cfs-greenline-20230708-053200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/113/08/mango-cfs-greenline-20230423-080400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/119/10/mango-cfs-greenline-20230429-103000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/111/06/mango-cfs-greenline-20230421-064200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/087/11/mango-cfs-greenline-20230328-110000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/101/06/mango-cfs-greenline-20230411-063800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/116/07/mango-cfs-greenline-20230426-073400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/109/08/mango-cfs-greenline-20230419-081800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/107/09/mango-cfs-greenline-20230417-094000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/143/08/mango-cfs-greenline-20230523-084800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/077/03/mango-cfs-greenline-20230318-032800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/103/05/mango-cfs-greenline-20230413-054200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/083/07/mango-cfs-greenline-20230324-075000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/085/06/mango-cfs-greenline-20230326-064000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/150/10/mango-cfs-greenline-20230530-100600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/178/06/mango-cfs-greenline-20230627-064000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/166/08/mango-cfs-greenline-20230615-080000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/058/07/mango-cfs-greenline-20230227-074600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/183/10/mango-cfs-greenline-20230702-100000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/195/08/mango-cfs-greenline-20230714-083000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/169/05/mango-cfs-greenline-20230618-053800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/190/07/mango-cfs-greenline-20230709-073200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/176/06/mango-cfs-greenline-20230625-062800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/180/10/mango-cfs-greenline-20230629-100400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/144/06/mango-cfs-greenline-20230524-060800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/170/07/mango-cfs-greenline-20230619-074400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/201/07/mango-cfs-greenline-20230720-074200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/192/07/mango-cfs-greenline-20230711-073600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/019/06/mango-cfs-greenline-20230119-063600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/021/04/mango-cfs-greenline-20230121-043600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/042/06/mango-cfs-greenline-20230211-064200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/274/03/mango-cfs-greenline-20240930-035000.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/140/07/mango-cfs-greenline-20230520-073000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/248/04/mango-cfs-greenline-20240904-044600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/144/06/mango-cfs-greenline-20230524-065000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/171/08/mango-cfs-greenline-20230620-080000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/147/09/mango-cfs-greenline-20230527-095000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/246/03/mango-cfs-greenline-20240902-035000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/238/04/mango-cfs-greenline-20240825-043400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/133/08/mango-cfs-greenline-20230513-080000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/166/05/mango-cfs-greenline-20230615-053200.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/221/07/mango-cfs-greenline-20240808-072400.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/218/04/mango-cfs-greenline-20240805-044400.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/217/07/mango-cfs-greenline-20240804-070400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/089/08/mango-cfs-greenline-20230330-085000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/108/08/mango-cfs-greenline-20230418-085200.hdf5', 'N'], #x, good example
    # ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2023/108/05/mango-cfs-greenline-20230418-054000.hdf5', 'N'], #187 same day doesn't count
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/005/09/mango-cvo-redline-20240105-092400.hdf5', 'Y'], #CVO RedLine Start: 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/041/07/mango-cvo-redline-20240210-073200.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/089/04/mango-cvo-redline-20240329-040400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/097/05/mango-cvo-redline-20240406-051600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/134/08/mango-cvo-redline-20240513-082800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/148/07/mango-cvo-redline-20240527-071600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/270/04/mango-cvo-redline-20240926-040800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/346/06/mango-cvo-redline-20221212-060800.hdf5', 'N'], #x (check again later if necessary)
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/113/06/mango-cvo-redline-20220423-060800.hdf5', 'Y'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/113/08/mango-cvo-redline-20220423-081200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/139/08/mango-cvo-redline-20220519-080400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/144/07/mango-cvo-redline-20220524-071600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/148/09/mango-cvo-redline-20220528-090400.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/251/06/mango-cvo-redline-20240907-060800.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/185/08/mango-cvo-redline-20220704-082400.hdf5', 'N'], #s
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/180/09/mango-cvo-redline-20220629-091200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/272/06/mango-cvo-redline-20220929-060800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/281/12/mango-cvo-redline-20221008-123200.hdf5', 'Y'], #done with CVO clear images (need 7 more cloudy from this line)
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/295/05/mango-cvo-redline-20221022-050000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/299/04/mango-cvo-redline-20221026-040400.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/316/02/mango-cvo-redline-20221112-022800.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/327/02/mango-cvo-redline-20221123-022800.hdf5', 'N'], #x water on lens
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/333/07/mango-cvo-redline-20221129-074000.hdf5', 'N'], #x
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/238/04/mango-cvo-redline-20240825-045600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2022/360/04/mango-cvo-redline-20221226-043200.hdf5', 'N'], #x

    #Below this line are images added for publication (unify red-green algoritm)
    #Site CFS, Utah
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/246/03/mango-cfs-redline-20240902-032800.hdf5', 'N'], #Started Here Sept 8
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/244/07/mango-cfs-redline-20240831-074000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/236/04/mango-cfs-redline-20240823-041200.hdf5', 'N'], #don't remove this one, great cloudy example, check video footage
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/235/04/mango-cfs-redline-20240822-043600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/231/04/mango-cfs-redline-20240818-041600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/220/04/mango-cfs-redline-20240807-041200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/120/09/mango-cfs-redline-20240429-090800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/123/06/mango-cfs-redline-20240502-064400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/283/09/mango-cfs-redline-20231010-094400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/259/07/mango-cfs-redline-20230916-071200.hdf5', 'Y'], #35 red here

    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/181/09/mango-cfs-redline-20230630-093600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/162/08/mango-cfs-redline-20230611-084800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/321/02/mango-cfs-redline-20221117-024000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/305/07/mango-cfs-redline-20221101-073600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/295/09/mango-cfs-redline-20221022-092400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/233/04/mango-cfs-redline-20220821-041600.hdf5', 'N'], #check clarity on this one
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/196/06/mango-cfs-redline-20220715-062400.hdf5', 'N'], #check clarity on this one
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/152/05/mango-cfs-redline-20220601-050400.hdf5', 'N'], #check clarity on this one
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/088/03/mango-cfs-redline-20220329-031600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/001/02/mango-cfs-redline-20220101-023200.hdf5', 'N'], #45 here and check quality (jan 01/2022 is image date) 

    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2022/082/03/mango-cfs-redline-20220323-033200.hdf5', 'Y'], #Started here sept 9
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/364/05/mango-cfs-redline-20211230-051600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/334/05/mango-cfs-redline-20211130-052000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/299/04/mango-cfs-redline-20211026-045600.hdf5', 'N'], #this one has many visible stars, but if it isn't like 100% CLEAR, it isn't clear
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/275/08/mango-cfs-redline-20211002-080400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/243/09/mango-cfs-redline-20210831-091200.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2021/228/07/mango-cfs-redline-20210816-075200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/112/03/mango-cfs-redline-20230422-034400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/138/07/mango-cfs-redline-20230518-074800.hdf5', 'N'], #review this, 55 here

    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/173/08/mango-cfs-redline-20230622-080800.hdf5', 'Y'], #Started here sept 10
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/204/09/mango-cfs-redline-20230723-092000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/252/07/mango-cfs-redline-20230909-071200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/316/06/mango-cfs-redline-20231112-065600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/351/07/mango-cfs-redline-20231217-072800.hdf5', 'Y'], #60 Here. Need more cloudy images
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2023/357/02/mango-cfs-redline-20231223-022400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/033/06/mango-cfs-redline-20240202-064800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/068/03/mango-cfs-redline-20240308-033200.hdf5', 'N'], #while the stars are still relatively clear, this is a good example of a median image, in which case we lean to N
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/253/06/mango-cfs-redline-20240909-061600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/118/05/mango-cfs-redline-20240427-051600.hdf5', 'N'], #Another median image. 65 here. Change site
    #Site PAR, North Carolina
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/205/03/mango-par-redline-20240723-035600.hdf5', 'N'], #Started here sept 12
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/157/02/mango-par-redline-20240605-024800.hdf5', 'N'], #light example
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/123/04/mango-par-redline-20240502-041200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/120/02/mango-par-redline-20240429-020800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/086/01/mango-par-redline-20240326-015200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/031/05/mango-par-redline-20240131-052800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/230/07/mango-par-redline-20230818-074800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/164/07/mango-par-redline-20230613-070400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/313/05/mango-par-redline-20231109-050000.hdf5', 'Y'], #Not great
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/343/06/mango-par-redline-20231209-060400.hdf5', 'Y'], #75 here

    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/364/02/mango-par-redline-20231230-021600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2022/230/06/mango-par-redline-20220818-063200.hdf5', 'N'],
    #Site EIO, Iowa
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2022/249/02/mango-eio-redline-20220906-024000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2022/269/02/mango-eio-redline-20220926-020800.hdf5', 'Y'], #dirt on the lens. TBD what to do with this type of image. Issue is present with all images at this site
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2022/299/07/mango-eio-redline-20221026-073600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2022/326/05/mango-eio-redline-20221122-052000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2023/104/04/mango-eio-redline-20230414-042000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2023/169/06/mango-eio-redline-20230618-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2023/203/08/mango-eio-redline-20230722-084000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/eio/redline/raw/2023/237/03/mango-eio-redline-20230825-030800.hdf5', 'N'], #85 here. moon maybe present here? Review if it causes an issue. 
    #Site MTO, North Dakota
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/258/03/mango-mto-redline-20240914-033600.hdf5', 'N'], #Started here sept 14
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/222/05/mango-mto-redline-20240809-050800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/212/05/mango-mto-redline-20240730-052400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/165/07/mango-mto-redline-20240613-071200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/148/07/mango-mto-redline-20240527-072400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/100/05/mango-mto-redline-20240409-052000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/088/03/mango-mto-redline-20240328-034000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/032/04/mango-mto-redline-20240201-041200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/337/01/mango-mto-redline-20231203-014400.hdf5', 'Y'], #Is october 31 2023 an aurora? Didn't include, but check it out I guess
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/291/02/mango-mto-redline-20231018-020400.hdf5', 'N'], #95 here. Debatably cloudy, but bottom half was covered pretty well so I think it counts. If it isn't obviously clear, it's cloudy

    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/259/02/mango-mto-redline-20240915-023600.hdf5', 'N'] ,#Started here sept 15s
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/288/01/mango-mto-redline-20231015-014000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/258/04/mango-mto-redline-20230915-042000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/227/05/mango-mto-redline-20230815-054800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/196/06/mango-mto-redline-20230715-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/168/06/mango-mto-redline-20230617-061200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/102/05/mango-mto-redline-20230412-053200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/251/03/mango-mto-redline-20230908-034000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2023/206/05/mango-mto-redline-20230725-053200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/060/03/mango-mto-redline-20240229-032400.hdf5', 'Y'], #105 Here. 
    
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/243/06/mango-mto-redline-20240830-064000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/215/07/mango-mto-redline-20240802-072400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/198/06/mango-mto-redline-20240716-065600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/193/07/mango-mto-redline-20240711-074400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/188/07/mango-mto-redline-20240706-073200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/183/07/mango-mto-redline-20240701-071600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/174/06/mango-mto-redline-20240622-060000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/162/06/mango-mto-redline-20240610-064800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/156/07/mango-mto-redline-20240604-070800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/137/05/mango-mto-redline-20240516-052400.hdf5', 'N'], #115 Here.
    #Site PAR, North Carolina
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/150/04/mango-par-redline-20240529-040000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/181/05/mango-par-redline-20240629-052800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/193/08/mango-par-redline-20240711-080800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/242/03/mango-par-redline-20240829-032000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/253/01/mango-par-redline-20240909-013200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/017/05/mango-par-redline-20240117-051600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/012/03/mango-par-redline-20240112-030400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/005/03/mango-par-redline-20240105-033200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/337/00/mango-par-redline-20231203-003200.hdf5', 'N'], #Iffy
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/278/01/mango-par-redline-20231005-010800.hdf5', 'N'], #125 Here.

    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/180/07/mango-par-redline-20230629-074400.hdf5', 'N'], #Sept 16 start
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/172/06/mango-par-redline-20230621-062800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/168/05/mango-par-redline-20230617-051600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/130/04/mango-par-redline-20230510-042000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/121/09/mango-par-redline-20230501-090400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/110/05/mango-par-redline-20230420-052800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/098/03/mango-par-redline-20230408-033600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/075/04/mango-par-redline-20230316-040400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/072/01/mango-par-redline-20230313-012800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/052/02/mango-par-redline-20230221-025600.hdf5', 'N'], #135 Here. Maybe check it? Faint dots are not stars on this, check video to be sure
#https://www.mangonetwork.org/mango/v1/database/sites/par/redline/2022-09-29 What is this lol
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/049/02/mango-par-redline-20230218-024800.hdf5', 'Y'], #Sept 17 Start
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/047/01/mango-par-redline-20230216-010000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/041/00/mango-par-redline-20230210-005200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/027/04/mango-par-redline-20230127-043600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/015/04/mango-par-redline-20230115-040400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2023/012/00/mango-par-redline-20230112-004800.hdf5', 'N'], #Very clearly cloudy. Small faded dots are NOT stars
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2022/356/02/mango-par-redline-20221222-020400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2022/354/06/mango-par-redline-20221220-065600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2022/302/02/mango-par-redline-20221029-022400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2022/358/03/mango-par-redline-20221224-034000.hdf5', 'Y'], #145 here
    #Site CVO, Oregon
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/320/03/mango-cvo-redline-20231116-030000.hdf5', 'N'], #Sept 20 Start
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/319/03/mango-cvo-redline-20231115-034000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/317/08/mango-cvo-redline-20231113-081200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/314/06/mango-cvo-redline-20231110-060800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/310/02/mango-cvo-redline-20231106-024400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/292/06/mango-cvo-redline-20231019-060000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/226/06/mango-cvo-redline-20230814-063200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/203/07/mango-cvo-redline-20230722-072400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/200/08/mango-cvo-redline-20230719-080800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/173/07/mango-cvo-redline-20230622-072000.hdf5', 'Y'], #155 Here.
#https://www.mangonetwork.org/mango/v1/database/sites/cvo/redline/2023-03-24 <-- aurora??
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/141/05/mango-cvo-redline-20230521-054800.hdf5', 'N'], #Sept 21 Start
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/140/05/mango-cvo-redline-20230520-054800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/138/09/mango-cvo-redline-20230518-091600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/136/05/mango-cvo-redline-20230516-055600.hdf5', 'N'], #Raindrops on lens. Not significant, but worth review
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/134/07/mango-cvo-redline-20230514-070800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/132/07/mango-cvo-redline-20230512-071600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/113/05/mango-cvo-redline-20230423-054800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/112/04/mango-cvo-redline-20230422-045200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/110/10/mango-cvo-redline-20230420-102000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/081/05/mango-cvo-redline-20230322-052800.hdf5', 'Y'], #165 Here.

    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/079/04/mango-cvo-redline-20230320-042000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/077/06/mango-cvo-redline-20230318-060800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/075/07/mango-cvo-redline-20230316-070400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/071/06/mango-cvo-redline-20230312-064800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/053/05/mango-cvo-redline-20230222-051200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/050/05/mango-cvo-redline-20230219-051200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/048/06/mango-cvo-redline-20230217-062000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/072/04/mango-cvo-redline-20230313-043200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/082/05/mango-cvo-redline-20230323-051600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2023/102/05/mango-cvo-redline-20230412-050800.hdf5', 'N'], #175 Here.

    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2024/072/08/mango-mro-greenline-20240312-084600.hdf5', 'N'], #need to add 61 cloudy greens from here
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2024/067/02/mango-mro-greenline-20240307-024600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/283/04/mango-mro-greenline-20231010-042200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/275/02/mango-mro-greenline-20231002-024000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/260/05/mango-mro-greenline-20230917-050200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/253/06/mango-mro-greenline-20230910-060400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/239/09/mango-mro-greenline-20230827-093000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/231/05/mango-mro-greenline-20230819-052400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/229/06/mango-mro-greenline-20230817-060400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/103/07/mango-mro-greenline-20230413-073400.hdf5', 'N'], #51 left

    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/081/04/mango-mro-greenline-20230322-045000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/043/02/mango-mro-greenline-20230212-023000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mro/greenline/raw/2023/011/03/mango-mro-greenline-20230111-032201.hdf5', 'N'], #Site NEW, Washington 
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/284/03/mango-new-greenline-20241010-030000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/279/03/mango-new-greenline-20241005-032600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/270/03/mango-new-greenline-20240926-034800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/217/07/mango-new-greenline-20240804-073600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/213/06/mango-new-greenline-20240731-060400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/200/06/mango-new-greenline-20240718-063200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/182/07/mango-new-greenline-20240630-072600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/179/07/mango-new-greenline-20240627-073600.hdf5', 'N'], #40 left

    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/166/08/mango-new-greenline-20240614-081200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/new/greenline/raw/2024/148/06/mango-new-greenline-20240527-065000.hdf5', 'N'], #Site BLO, Bear Lake, Utah
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/247/05/mango-blo-greenline-20240903-053400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/222/09/mango-blo-greenline-20240809-092200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/219/06/mango-blo-greenline-20240806-065400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/210/04/mango-blo-greenline-20240728-045400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/159/05/mango-blo-greenline-20240607-052600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/150/05/mango-blo-greenline-20240529-050600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/127/05/mango-blo-greenline-20240506-051400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/099/07/mango-blo-greenline-20240408-070200.hdf5', 'N'], #30 left

    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/096/04/mango-blo-greenline-20240405-040400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/090/04/mango-blo-greenline-20240330-041400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/036/06/mango-blo-greenline-20240205-063000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/033/03/mango-blo-greenline-20240202-031200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/337/02/mango-blo-greenline-20231203-022400.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/320/04/mango-blo-greenline-20231116-043000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/311/02/mango-blo-greenline-20231107-025800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/309/02/mango-blo-greenline-20231105-020600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/307/04/mango-blo-greenline-20231103-043400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/286/03/mango-blo-greenline-20231013-031800.hdf5', 'N'], #20 left

    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/284/10/mango-blo-greenline-20231011-100200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/262/03/mango-blo-greenline-20230919-031800.hdf5', 'N'], #check this
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/257/05/mango-blo-greenline-20230914-052800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/231/09/mango-blo-greenline-20230819-091200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/200/05/mango-blo-greenline-20230719-053000.hdf5', 'N'], 
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/164/07/mango-blo-greenline-20230613-074200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/159/06/mango-blo-greenline-20230608-063200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/133/04/mango-blo-greenline-20230513-045000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2023/108/04/mango-blo-greenline-20230418-041400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/298/03/mango-blo-greenline-20221025-033000.hdf5', 'N'], #10 left

    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/272/05/mango-blo-greenline-20220929-055400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/238/08/mango-blo-greenline-20220826-081800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/237/04/mango-blo-greenline-20220825-044600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/232/04/mango-blo-greenline-20220820-043000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/214/05/mango-blo-greenline-20220802-050400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/204/07/mango-blo-greenline-20220723-071000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/184/06/mango-blo-greenline-20220703-060400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/175/09/mango-blo-greenline-20220624-092600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/150/05/mango-blo-greenline-20220530-051800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2022/147/06/mango-blo-greenline-20220527-064200.hdf5', 'N'], #done greens

    #25 clear reds remaining, 31 cloudy reds.
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/297/02/mango-mto-redline-20241023-020400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/283/10/mango-mto-redline-20241009-105200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/281/10/mango-mto-redline-20241007-102800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/279/09/mango-mto-redline-20241005-091200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/277/08/mango-mto-redline-20241003-085600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/275/07/mango-mto-redline-20241001-074000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/297/05/mango-cvo-redline-20241023-051600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/295/02/mango-cvo-redline-20241021-024800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/276/08/mango-cvo-redline-20241002-081200.hdf5', 'Y'], #bad quality, still clear though
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/272/09/mango-cvo-redline-20240928-093200.hdf5', 'Y'],

    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/299/02/mango-par-redline-20241025-024400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/280/02/mango-par-redline-20241006-025200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/278/00/mango-par-redline-20241004-005600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/287/04/mango-mdk-redline-20231014-040000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/286/03/mango-mdk-redline-20231013-030400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/284/06/mango-mdk-redline-20231011-060400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/282/05/mango-mdk-redline-20231009-051600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/278/01/mango-mdk-redline-20231005-014400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/259/02/mango-mdk-redline-20230916-024400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/257/05/mango-mdk-redline-20230914-050800.hdf5', 'Y'],

    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/250/02/mango-mdk-redline-20230907-023200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/231/05/mango-mdk-redline-20230819-050400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/226/03/mango-mdk-redline-20230814-031600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/223/03/mango-mdk-redline-20230811-035200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/197/06/mango-mdk-redline-20230716-063600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/195/05/mango-mdk-redline-20230714-052000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/194/05/mango-mdk-redline-20230713-052000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/190/03/mango-mdk-redline-20230709-035200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/171/06/mango-mdk-redline-20230620-062800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/169/04/mango-mdk-redline-20230618-040800.hdf5', 'N'],
    
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/167/07/mango-mdk-redline-20230616-075600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/165/05/mango-mdk-redline-20230614-050400.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/162/03/mango-mdk-redline-20230611-035600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/137/04/mango-mdk-redline-20230517-040000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/136/03/mango-mdk-redline-20230516-032800.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/134/03/mango-mdk-redline-20230514-035600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/132/06/mango-mdk-redline-20230512-065200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/130/04/mango-mdk-redline-20230510-040400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/128/04/mango-mdk-redline-20230508-041200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/110/09/mango-mdk-redline-20230420-091600.hdf5', 'N'],
    
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/104/04/mango-mdk-redline-20230414-044800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/082/05/mango-mdk-redline-20230323-054000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/080/03/mango-mdk-redline-20230321-034400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/078/04/mango-mdk-redline-20230319-042800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/071/02/mango-mdk-redline-20230312-020400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/048/01/mango-mdk-redline-20230217-015200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/300/06/mango-cfs-redline-20241026-062000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/283/10/mango-cfs-redline-20241009-105600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/280/04/mango-cfs-redline-20241006-044800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/277/07/mango-cfs-redline-20241003-074400.hdf5', 'Y'],

    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/275/10/mango-cfs-redline-20241001-103200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/273/09/mango-cfs-redline-20240929-092400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/270/03/mango-cfs-redline-20240926-034000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/254/10/mango-cfs-redline-20240910-100000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/redline/raw/2024/252/04/mango-cfs-redline-20240908-043600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/redline/raw/2024/303/03/mango-cvo-redline-20241029-030000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/301/00/mango-par-redline-20241027-002400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/298/01/mango-par-redline-20241024-015600.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/302/01/mango-mto-redline-20241028-012400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/299/03/mango-mto-redline-20241025-032000.hdf5', 'Y'],

    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/305/06/mango-mto-redline-20241031-065200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/304/01/mango-mto-redline-20241030-014400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/286/09/mango-mto-redline-20241012-091200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mto/redline/raw/2024/284/05/mango-mto-redline-20241010-052800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/305/00/mango-par-redline-20241031-002400.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/par/redline/raw/2024/304/00/mango-par-redline-20241030-001600.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/047/02/mango-mdk-redline-20230216-020000.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2023/045/03/mango-mdk-redline-20230214-031200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2022/121/04/mango-mdk-redline-20220501-045200.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2022/179/04/mango-mdk-redline-20220628-043600.hdf5', 'N'],

    #3 clear, 3 cloudy to finish this
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2022/269/07/mango-mdk-redline-20220926-072800.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2022/266/05/mango-mdk-redline-20220923-055200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2022/265/02/mango-mdk-redline-20220922-021200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2022/263/03/mango-mdk-redline-20220920-034000.hdf5', 'Y'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2022/261/04/mango-mdk-redline-20220918-041200.hdf5', 'N'],
    ['https://data.mangonetwork.org/data/transport/mango/archive/mdk/redline/raw/2022/239/09/mango-mdk-redline-20220827-090000.hdf5', 'Y'],

    # #switch between 5 cloudy and 5 clear, then red / green
    # ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2024/312/06/mango-bdr-greenline-20241107-062600.hdf5', 'N'],
    # ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2024/310/01/mango-bdr-greenline-20241105-015800.hdf5', 'N'],
    # ['https://data.mangonetwork.org/data/transport/mango/archive/bdr/greenline/raw/2024/306/01/mango-bdr-greenline-20241101-013600.hdf5', 'Y'],
    # ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/311/03/mango-blo-greenline-20241106-031000.hdf5', 'Y'],
    # ['https://data.mangonetwork.org/data/transport/mango/archive/blo/greenline/raw/2024/309/06/mango-blo-greenline-20241104-061200.hdf5', 'Y'],
    # ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/308/05/mango-cfs-greenline-20241103-053400.hdf5', 'N'], #check
    # ['https://data.mangonetwork.org/data/transport/mango/archive/cfs/greenline/raw/2024/295/02/mango-cfs-greenline-20241021-025200.hdf5', 'Y'],
    # ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/greenline/raw/2024/308/02/mango-cvo-greenline-20241103-024000.hdf5', 'N'], #check
    # ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/greenline/raw/2024/301/03/mango-cvo-greenline-20241027-033800.hdf5', 'Y'],
    # ['https://data.mangonetwork.org/data/transport/mango/archive/cvo/greenline/raw/2024/300/04/mango-cvo-greenline-20241026-043400.hdf5', 'N'] #check
    
    










    ]

    return urls