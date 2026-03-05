# Toposolid Host Topo Id Property

Source: https://www.revitapidocs.com/2026/d16ba5b3-da97-b262-3dc8-5de0a9816f74.htm

---

| Toposolid Host Topo Id Property |
| --- |

The host Toposolid id of the current Toposolid subdivision.
 If the object is not a Toposolid subdivision, hostTopoId will be InvalidElementId. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId HostTopoId { get; }
```

```
Public ReadOnly Property HostTopoId As ElementId
	Get
```

```
public:
property ElementId^ HostTopoId {
	ElementId^ get ();
}
```

```
member HostTopoId : ElementId with get
```

#### Property Value

[ElementId](Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
