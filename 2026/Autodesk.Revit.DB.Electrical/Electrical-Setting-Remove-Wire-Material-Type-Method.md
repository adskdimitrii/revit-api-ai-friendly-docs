# Electrical Setting Remove Wire Material Type Method

Source: https://www.revitapidocs.com/2026/d3193518-abc6-0c64-cbf8-332b04bef8ad.htm

---

| Electrical Setting Remove Wire Material Type Method |
| --- |

**Note: This API is now obsolete.** 

Remove the wire material type from project. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("RemoveWireMaterialType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use Document.Delete() instead.")]
public void RemoveWireMaterialType(
	WireMaterialType materialType
)
```

```
<ObsoleteAttribute("RemoveWireMaterialType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use Document.Delete() instead.")>
Public Sub RemoveWireMaterialType ( 
	materialType As WireMaterialType
)
```

```
public:
[ObsoleteAttribute(L"RemoveWireMaterialType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use Document.Delete() instead.")]
void RemoveWireMaterialType(
	WireMaterialType^ materialType
)
```

```
[<ObsoleteAttribute("RemoveWireMaterialType is deprecated in Revit 2026 and will be removed in a future version of Revit. Please use Document.Delete() instead.")>]
member RemoveWireMaterialType : 
        materialType : WireMaterialType -> unit 
```

#### Parameters

materialType [WireMaterialType](Wire-Material-Type-Class.md)
:   The wire material type to be removed.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Wire material type can be removed only if it is not currently assigned to any wire type,  and the last one wire material type can't be removed, otherwise an exception will be thrown. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSetting Class](Electrical-Setting-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
