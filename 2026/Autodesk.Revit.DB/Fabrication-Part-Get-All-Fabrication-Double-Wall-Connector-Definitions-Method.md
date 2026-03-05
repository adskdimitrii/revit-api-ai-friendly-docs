# Fabrication Part Get All Fabrication Double Wall Connector Definitions Method

Source: https://www.revitapidocs.com/2026/45aa54c1-6aaf-f239-2891-a57ef35c0ef2.htm

---

| Fabrication Part Get All Fabrication Double Wall Connector Definitions Method |
| --- |

Gets all connectors that are valid to be assigned to the part for a specified double wall connector 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<int> GetAllFabricationDoubleWallConnectorDefinitions(
	Connector connector
)
```

```
Public Function GetAllFabricationDoubleWallConnectorDefinitions ( 
	connector As Connector
) As IList(Of Integer)
```

```
public:
IList<int>^ GetAllFabricationDoubleWallConnectorDefinitions(
	Connector^ connector
)
```

```
member GetAllFabricationDoubleWallConnectorDefinitions : 
        connector : Connector -> IList<int> 
```

#### Parameters

connector [Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)
:   The connector to to check against

#### Return Value

IList Int32 
Returns an array of connector database identifiers ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[FabricationPart Class](Fabrication-Part-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
