# Built In Failures Import Failures ATFNon Uniform Scaling Transform Property

Source: https://www.revitapidocs.com/2026/20ac0edb-b4da-951b-db57-a1ce2c2fa59b.htm

---

| Built In Failures Import Failures ATFNon Uniform Scaling Transform Property |
| --- |

**Note: This API is now obsolete.** 

The imported geometry contains non\-uniform scaling transformations which Revit does not support. Some objects may be displaced or distorted. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This failure is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use ImportContainedUnsupportedTransform instead.")]
public static FailureDefinitionId ATFNonUniformScalingTransform { get; }
```

```
<ObsoleteAttribute("This failure is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use ImportContainedUnsupportedTransform instead.")>
Public Shared ReadOnly Property ATFNonUniformScalingTransform As FailureDefinitionId
	Get
```

```
public:
[ObsoleteAttribute(L"This failure is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use ImportContainedUnsupportedTransform instead.")]
static property FailureDefinitionId^ ATFNonUniformScalingTransform {
	FailureDefinitionId^ get ();
}
```

```
[<ObsoleteAttribute("This failure is deprecated in Revit 2026 and may be removed in a later version of Revit. We suggest you use ImportContainedUnsupportedTransform instead.")>]
static member ATFNonUniformScalingTransform : FailureDefinitionId with get
```

#### Property Value

[FailureDefinitionId](b6ada360-a6fe-ebb6-b095-d74b37ade9bf.htm) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[BuiltInFailures ImportFailures Class](Built-In-Failures-Import-Failures-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
