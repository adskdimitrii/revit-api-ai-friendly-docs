# Energy Data Settings Get Energy Data Settings Method

Source: https://www.revitapidocs.com/2026/d7fd4001-4bd7-7b38-1800-0b03baf989ec.htm

---

| Energy Data Settings Get Energy Data Settings Method |
| --- |

Gets the energy data settings element in the document. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static EnergyDataSettings GetEnergyDataSettings(
	Document doc
)
```

```
Public Shared Function GetEnergyDataSettings ( 
	doc As Document
) As EnergyDataSettings
```

```
public:
static EnergyDataSettings^ GetEnergyDataSettings(
	Document^ doc
)
```

```
static member GetEnergyDataSettings : 
        doc : Document -> EnergyDataSettings 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document where the settings element is found.

#### Return Value

[EnergyDataSettings](Energy-Data-Settings-Class.md) 
The element which stores the energy data settings for the document. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[EnergyDataSettings Class](Energy-Data-Settings-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
