# Energy Analysis Space Get Boundary Method

Source: https://www.revitapidocs.com/2026/34f9d5ec-7195-0324-60a4-a2d51d8b2ab8.htm

---

| Energy Analysis Space Get Boundary Method |
| --- |

Gets the collection of polygons that form the 2D boundary.
 This method returns a collection of polyloops (planar
 polygons) that defines an enclosed area measured by
 interior bounding surfaces, if in rooms and spaces mode.
 In other modes, returns no polyloops. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<Polyloop> GetBoundary()
```

```
Public Function GetBoundary As IList(Of Polyloop)
```

```
public:
IList<Polyloop^>^ GetBoundary()
```

```
member GetBoundary : unit -> IList<Polyloop> 
```

#### Return Value

IList [Polyloop](207c5546-9116-fb85-8a7e-ff79654a7877.htm) 
The collection of polygons that form the 2D boundary. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[EnergyAnalysisSpace Class](Energy-Analysis-Space-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
