# Energy Analysis Space Get Closed Shell Method

Source: https://www.revitapidocs.com/2026/58410893-1269-98e3-7a07-e5dacafbc9fe.htm

---

| Energy Analysis Space Get Closed Shell Method |
| --- |

Gets the collection of polygons that form a closed shell.
 This method returns a collection of polyloops (planar
 polygons) that defines an enclosed volume measured by
 interior bounding surfaces, if in rooms and spaces mode.
 In other modes, returns no polyloops. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<Polyloop> GetClosedShell()
```

```
Public Function GetClosedShell As IList(Of Polyloop)
```

```
public:
IList<Polyloop^>^ GetClosedShell()
```

```
member GetClosedShell : unit -> IList<Polyloop> 
```

#### Return Value

IList [Polyloop](207c5546-9116-fb85-8a7e-ff79654a7877.htm) 
the collection of polygons that form a closed shell. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[EnergyAnalysisSpace Class](Energy-Analysis-Space-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
