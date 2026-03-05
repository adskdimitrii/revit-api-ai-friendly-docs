# Label Utils Get Label For(gb XMLBuilding Type, Document) Method

Source: https://www.revitapidocs.com/2026/3e86f8bf-b9b6-5383-3f65-0a9c9a5acf61.htm

---

| Label Utils Get Label For(gb XMLBuilding Type, Document) Method |
| --- |

Gets the user\-visible name for a gbXMLBuildingType. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static string GetLabelFor(
	gbXMLBuildingType buildingType,
	Document document
)
```

```
Public Shared Function GetLabelFor ( 
	buildingType As gbXMLBuildingType,
	document As Document
) As String
```

```
public:
static String^ GetLabelFor(
	gbXMLBuildingType buildingType, 
	Document^ document
)
```

```
static member GetLabelFor : 
        buildingType : gbXMLBuildingType * 
        document : Document -> string 
```

#### Parameters

buildingType [gbXMLBuildingType](74e09dc3-6b9a-cc3b-a493-d6a20a60bfd6.htm)
:   The gbXMLBuildingType to get the user\-visible name.

document [Document](Document-Class.md)
:   The document from which to get the gbXMLBuildingType.

#### Return Value

String 
Returns the user\-visible name for a buildingType in gbXML. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input gXMLBuildingType is not available in the document. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The name is obtained in the current Revit language. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[LabelUtils Class](Label-Utils-Class.md) [GetLabelFor Overload](39e41221-70f9-fae6-53e6-872eff5a2c63.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
