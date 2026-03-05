# Rebar Container Contains Method

Source: https://www.revitapidocs.com/2026/ed75fef3-8c01-c440-a1ca-db20914712fa.htm

---

| Rebar Container Contains Method |
| --- |

Checks if the RebarContainer has this item as one of its members. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool Contains(
	RebarContainerItem item
)
```

```
Public Function Contains ( 
	item As RebarContainerItem
) As Boolean
```

```
public:
bool Contains(
	RebarContainerItem^ item
)
```

```
member Contains : 
        item : RebarContainerItem -> bool 
```

#### Parameters

item [RebarContainerItem](Rebar-Container-Item-Class.md)
:   The item to be checked if RebarContainer has it as one of its members

#### Return Value

Boolean 
True if RebarContainer has this item as one of its members, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainer Class](Rebar-Container-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
