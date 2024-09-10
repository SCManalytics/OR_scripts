\* ABC_Cosmetic_Co._Distribution_Problem *\
Minimize
Sum_of_Transporting_Costs: 8 Route_PlantA_C1 + 7 Route_PlantA_C2
 + 5 Route_PlantA_C3 + 2 Route_PlantA_C4 + 5 Route_PlantB_C1
 + 2 Route_PlantB_C2 + Route_PlantB_C3 + 3 Route_PlantB_C4 + 6 Route_PlantC_C1
 + 4 Route_PlantC_C2 + 3 Route_PlantC_C3 + 5 Route_PlantC_C4
Subject To
Sum_of_Products_into_client_C1: Route_PlantA_C1 + Route_PlantB_C1
 + Route_PlantC_C1 + Route_PlantD_C1 >= 22
Sum_of_Products_into_client_C2: Route_PlantA_C2 + Route_PlantB_C2
 + Route_PlantC_C2 + Route_PlantD_C2 >= 27
Sum_of_Products_into_client_C3: Route_PlantA_C3 + Route_PlantB_C3
 + Route_PlantC_C3 + Route_PlantD_C3 >= 23
Sum_of_Products_into_client_C4: Route_PlantA_C4 + Route_PlantB_C4
 + Route_PlantC_C4 + Route_PlantD_C4 >= 28
Sum_of_Products_out_of_Warehouse_PlantA: Route_PlantA_C1 + Route_PlantA_C2
 + Route_PlantA_C3 + Route_PlantA_C4 <= 30
Sum_of_Products_out_of_Warehouse_PlantB: Route_PlantB_C1 + Route_PlantB_C2
 + Route_PlantB_C3 + Route_PlantB_C4 <= 30
Sum_of_Products_out_of_Warehouse_PlantC: Route_PlantC_C1 + Route_PlantC_C2
 + Route_PlantC_C3 + Route_PlantC_C4 <= 30
Sum_of_Products_out_of_Warehouse_PlantD: Route_PlantD_C1 + Route_PlantD_C2
 + Route_PlantD_C3 + Route_PlantD_C4 <= 10
Bounds
 0 <= Route_PlantA_C1
 0 <= Route_PlantA_C2
 0 <= Route_PlantA_C3
 0 <= Route_PlantA_C4
 0 <= Route_PlantB_C1
 0 <= Route_PlantB_C2
 0 <= Route_PlantB_C3
 0 <= Route_PlantB_C4
 0 <= Route_PlantC_C1
 0 <= Route_PlantC_C2
 0 <= Route_PlantC_C3
 0 <= Route_PlantC_C4
 0 <= Route_PlantD_C1
 0 <= Route_PlantD_C2
 0 <= Route_PlantD_C3
 0 <= Route_PlantD_C4
Generals
Route_PlantA_C1
Route_PlantA_C2
Route_PlantA_C3
Route_PlantA_C4
Route_PlantB_C1
Route_PlantB_C2
Route_PlantB_C3
Route_PlantB_C4
Route_PlantC_C1
Route_PlantC_C2
Route_PlantC_C3
Route_PlantC_C4
Route_PlantD_C1
Route_PlantD_C2
Route_PlantD_C3
Route_PlantD_C4
End
